
from django.db import models
from django.core.validators import MinLengthValidator

class User(models.Model):
    name = models.CharField("Name", max_length=100)
    email = models.CharField("E-mail", max_length=80)
    password = models.CharField("Password", max_length=18, validators = [MinLengthValidator])

    def __str__(self):
        return self.name
        
class LogEntry(models.Model):
    title = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=200, blank="", null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField
    isArchived = models.BooleanField(default=False)
    colectedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    CATEGORIES = [
            ('PROD','Produção'),
            ('HOMO','Homologação'),
            ('DEV', 'Desenvolvimento')
        ]
    category = models.CharField(max_length=20, choices=CATEGORIES, default='PROD')
    LEVELS = [
            ('ERROR', 'ERROR'),
            ('DEBUG', 'DEBUG'),
            ('WARNING', 'WARNING')
        ]
    level = models.CharField(max_length=8, choices=LEVELS, default='ERROR')
    
    class Meta:
        ordering = ['createdAt']
    
    def __str__(self):
        return self.description