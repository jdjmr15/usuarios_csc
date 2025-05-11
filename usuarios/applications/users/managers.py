from django.db import models

from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager, models.Manager):
    """
    Custom user manager for User model
    """

    def _create_user(self, username, email, password=None, is_staff=False, is_superuser=False, **extra_fields):
        user = self.model(
            username=username,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password, **extra_fields):
        """
        Create and return a superuser with an email and password
        """
        return self._create_user(username, email, password, True, True, **extra_fields)