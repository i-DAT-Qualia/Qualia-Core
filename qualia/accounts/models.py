from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.conf import settings


class QualiaUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=QualiaUserManager.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password
        )
        user.level = 5
        user.save(using=self._db)
        return user

    def create_dashboard_user(self, email, password, org_id):
        user = self.create_user(
            email,
            password=password
        )
        user.level = 2
        user.save(using=self._db)
        return user


class QualiaUser(AbstractBaseUser):
    objects = QualiaUserManager()

    email = models.EmailField(max_length=254, unique=True)
    is_active = models.BooleanField(default=True)
    is_beta = models.BooleanField(default=False)

    level_choices = (
        (5, 'Admin'),
        (4, 'System Super'),
        (3, 'Org Super'),
        (2, 'Org User'),
        (1, 'User'),
    )

    level = models.IntegerField(default=1, choices=level_choices)

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # Handle whether the user has a specific permission?"
        return True

    def has_module_perms(self, app_label):
        # Handle whether the user has permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        '''
        Handles access to admin views, where admin is user level 5
        '''

        if self.level == 5:
            return True
        else:
            return False
