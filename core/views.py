from django.shortcuts import render
from django.db.models import Q
from django.db import transaction
from rest_framework import status
from django.conf import settings
from rest_framework import parsers, renderers
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework import viewsets
from django.http import Http404
import requests
from django.views.decorators.csrf import csrf_exempt
import json, re
from django.utils.crypto import get_random_string
from itertools import permutations
from itertools import compress, product
from .models import Processor
from .serializers import ProcessorSerializer


class ProcessorView(APIView):
    def post(self, request):
        city = request.data.get("city", "")
        state = request.data.get("state", "")
        text = request.data.get("text")
        url = request.data.get("url")
        if None in [url, text]:
            return Response({"message": "Request parameter missing"}, status=status.HTTP_400_BAD_REQUEST)

        if not validate_url(url):
            return Response({"message": "URL not valid"}, status=status.HTTP_400_BAD_REQUEST)

        # ==================  Tags Calculation start  ==================
        if city !="":
            text = text.strip()+" "+city
        if state !="":
            text = text+" "+state

        splited_text_arr = text.strip().split()
        temp_sta = []
        for sta in splited_text_arr:
            if sta not in temp_sta:
                temp_sta.append(sta)
        com_text_array = combinations(temp_sta)
        tags = []
        for ca in com_text_array:
            connected_string = ""
            for sca in ca:
                connected_string = connected_string + sca if connected_string == "" else connected_string + " " + sca
            tags.append(connected_string)
        empty_val = tags.pop(0)  # removing empty value

        # ==================  Tags Calculation End  ==================

        # ==================  Description Calculation Start  ==================
        description = text + " - " + url + " if you are looking for " + text + ", then watch this video to learn everything to know about " + text
        hash_tag_str = ""
        for tag in tags:
            hash_tag_str= hash_tag_str + "#"+tag+", "
        # ==================  Description Calculation End  ==================

        response = {
            "title": ' '.join(temp_sta).title(),
            "description": description,
            "description_tags":hash_tag_str.rstrip(', '),
            "tags": ', '.join(tags),
        }
        return Response(response, status=status.HTTP_200_OK)


def combinations(items):
    return (set(compress(items, mask)) for mask in product(*[[0, 1]] * len(items)))


def validate_url(url):
    regex = re.compile(
        r"^(?:http|ftp)s?://"  # http:// or https://
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain...
        r"localhost|"  # localhost...
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
        r"(?::\d+)?"  # optional port
        r"(?:/?|[/?]\S+)$", re.IGNORECASE)

    return re.match(regex, url) is not None  # True
