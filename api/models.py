from django.db import models

# Create your models here.

class cadastroUsuario(models.Model):
    email = models.CharField(max_length=70, blank=False, default='')
    password = models.CharField( min_length=12, blank=False, default='' )

class login(models.Model):
    email = models.CharField(max_length=70, blank=False,required=True,  default='')
    password = models.CharField( min_length=12, blank=False, required=True, default='' )