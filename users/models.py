from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.db import models



class UserManager(BaseUserManager):
    def create_user(self,email,name,password=None, **extra):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, name, password=None, **extra):
        email = models.EmailField(unique=True)
        name = models.CharField(max_length=150)
        subscription = models.ForeignKey(
            'subscriptions.Subscription',
            on_delete= models.SET_NULL,
            nul=True, blank=True,
            related_names ='users',
        )
        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=False)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        objects = UserManager()

        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['name']

        class Meta:
            db_table = 'users'

        def __str__(self):
            return f'{self.name} <{self.email}>'