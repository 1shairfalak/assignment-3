from ctypes import addressof
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import (BaseUserManager, AbstractUser)
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    image = models.ImageField(upload_to = 'media/')
    city = models.CharField(max_length=200,default= "",null=False,blank=False)
    address = models.CharField(max_length=200,default="",null=False,blank=False)

    CNIC = models.CharField(max_length=200, default="", null=False, blank=False)
    D_O_B = models.DateField(max_length=8, null=True)
    mobile_number = PhoneNumberField(default="")
    def __str__(self):
        return self.username
    class Meta(object):
        verbose_name_plural = 'Users'
        verbose_name = 'User'
