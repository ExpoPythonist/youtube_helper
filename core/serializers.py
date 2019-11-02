from rest_framework import serializers
from django.utils.crypto import get_random_string
from django.db import transaction, IntegrityError
from rest_framework import exceptions
from rest_framework import status
from django.utils.translation import ugettext_lazy as _
from .models import Processor


# Create custom api exception
class CustomAPIException(exceptions.APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = 'error'

    def __init__(self, detail, status_code=None):
        self.detail = detail
        if status_code is not None:
            self.status_code = status_code


class ProcessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processor
        fields = ('id', 'text')
