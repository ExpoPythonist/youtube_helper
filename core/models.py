from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, _user_has_perm
)
from django.core.exceptions import ValidationError
from django.apps import apps
from rest_framework import serializers
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils.crypto import get_random_string


class Processor(models.Model):
    text = models.CharField(max_length=100, null=True, blank=True)