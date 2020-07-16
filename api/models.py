
from django.db import models
from django.core.validators import MinLengthValidator

category_CHOICES = [
    ('PROD','Produção'),
    ('HOMO','Homologação'),
    ('DEV', 'Desenvolvimento')
]


class User(models.Model):
    name = models.CharField("Name", max_length=100)
    email = models.CharField("E-mail")
    password = models.CharField("Password", max_length=18, validators = [MinLengthValidator])

    def __str__(self):
        return self.name
        

class LogEntry(models.Model):
    title = models.CharField(max_length=200)
    createdAt = models.DateTimeField
    updatedAt = models.DateTimeField
    isAArchived = models.BooleanField
    category = [category_CHOICES]