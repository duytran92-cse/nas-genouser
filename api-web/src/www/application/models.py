from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.core.signing import Signer
from . import constants
import uuid


class UserAchievement(models.Model):
    user =  models.ForeignKey('User', on_delete=models.CASCADE)
    name =  models.CharField(max_length=255, choices=constants.ACHIEVEMENTS, default='')


class User(models.Model):
    username =      models.CharField(max_length=255, unique=True)
    email   =       models.CharField(max_length=255, unique=True)
    password =      models.TextField()
    salt    =       models.TextField()
    joined_at  =    models.DateTimeField(auto_now_add=True)
    is_active =     models.BooleanField(default=True)
    is_deleted =    models.BooleanField(default=False)


class UserProfile(models.Model):
    user    =   models.OneToOneField('User', on_delete=models.CASCADE)
    fullname =  models.CharField(max_length=255, default='')
    position =  models.IntegerField(default=0)
    about   =   models.TextField(default='')
    gender  =   models.CharField(max_length=255, choices=constants.GENDER, default='male')
    country =   models.CharField(max_length=255, choices=constants.COUNTRIES, default='DEU')
    education = models.CharField(max_length=255, choices=constants.EDUCATION, default='bach')
    work    =   models.CharField(max_length=255, default='')
    photo   =   models.TextField(default='')
    rank    =   models.IntegerField(default=0)
    genetic_type = models.CharField(max_length=255, choices=constants.GENETIC_TYPE, default='novice')
    birthday     =   models.CharField(max_length=255, default='')
    account_paypal  = models.CharField(max_length=255, default='')
    science_filter = models.CharField(max_length=255, default='')


class UserContact(models.Model):
    user =          models.ForeignKey('User', related_name='user')
    friend =        models.ForeignKey('User', related_name='friend')
    timestamp   =   models.DateTimeField(default=timezone.now)


class UserMessage(models.Model):
    sender =    models.ForeignKey('User', related_name='sender')
    receiver =  models.ForeignKey('User', related_name='receiver')
    message =   models.TextField(default='')
    is_read =   models.BooleanField(default=False)
    sent_at =   models.DateTimeField(auto_now_add=True)


class UserResetPassToken(models.Model):
    user    =   models.ForeignKey('User', on_delete=models.CASCADE)
    token   =   models.CharField(max_length=255)
    created_at =models.DateTimeField(auto_now_add=True)

class UserNotification(models.Model):
    user = models.ForeignKey('User')
    kind = models.CharField(max_length=255, default="")
    message = models.TextField(default="")
    is_sent = models.BooleanField(default=False)

class Variation(models.Model):
    rsnumber =  models.CharField(max_length=255, default='')
    position =  models.IntegerField(default=0)
    chromosome   =   models.TextField(default='')
    genes  =   models.TextField(default='')
    publications =   models.TextField(default='')
    diseases = models.TextField(default='')
    effects = models.TextField(default='')
    science_filter = models.CharField(max_length=255, default='')

class UserVariation(models.Model):
    user    =   models.ForeignKey('User')
    rsnumber =  models.CharField(max_length=255, default='')
    position =  models.IntegerField(default=0)
    chromosome   =   models.TextField(default='')
    genotype    =   models.TextField(default='')
    

class UserUpload(models.Model):
    user = models.ForeignKey('User')
    filename = models.CharField(max_length=255, default="")
    text = models.TextField(default="", max_length=4294967295)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_disable = models.BooleanField(default=False)
