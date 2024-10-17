from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin,
)
from django.urls import reverse_lazy
from django.utils import timezone
# Create your models here.

class UserManager(BaseUserManager):
    
    def create_user(self, username, email, password = None):
        if not email:
            raise ValueError('Enter Email')
        user = self.model(
            username = username,
            email = email
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, username, email, password = None):
        user = self.model(
            username = username,
            email = email,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)#auto_now_addは、最初に作成された時のみ自動で作成される。
    update_at = models.DateTimeField(auto_now=True)#auto_nowは、更新されるたびに自動的に変更される。

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def get_absolute_url(self):
        return reverse_lazy('dishapp:dish_home')