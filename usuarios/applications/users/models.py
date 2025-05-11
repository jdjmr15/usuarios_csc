from django.db import models

from django.contrib.auth.models import AbstractUser, PermissionsMixin

# Create your models here.
from .managers import UserManager

class User(AbstractUser, PermissionsMixin):
    
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro')
    ]
    
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    nombres = models.CharField(max_length=50, blank=True)
    apellidos = models.CharField(max_length=50, blank=True)
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    objects = UserManager()
    
    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return f"{self.nombres} {self.apellidos}"

    def __str__(self):
        return self.username