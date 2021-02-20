from time import timezone
from django.utils import timezone, dateformat
from datetime import datetime
from django.db import models


class DocShopApp(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    country_code = models.BigIntegerField()
    phone_number = models.FloatField()
    password = models.CharField(max_length=255)



class Documents(models.Model):
    subject = models.TextField()
    description = models.TextField()
    wordcount = models.BigIntegerField()