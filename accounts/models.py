
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)



class UserAccountManager(BaseUserManager):

    def create_user(self, email, username, full_name, gender, phone_number, password=None, **extra_fields):
        if not email:
            raise ValueError(_('Users must have an email address'))
        if not username:
            raise ValueError(_('Users must have a username'))
        if not full_name:
            raise ValueError(_('Users must provide their full name'))

        if not gender:
            raise ValueError(_('Users must provide their gender'))
        if not phone_number:
            raise ValueError(_('Users must provide their phone number'))

        # phone_number.setdefault('is_staff', True)
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            full_name=full_name,
            gender=gender,
            phone_number=phone_number,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, full_name, gender, phone_number,
                         password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,

            full_name=full_name,

            gender=gender,
            phone_number=phone_number,

            password=password

        )
        # user.set_password(password)
        user.admin = True
        user.staff = True
        user.user_role = 1
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    # from Util.ListsOfData import CITIES_CHOICES, AREA_CHOICES
    from Util.ListsOfData import GENDER_CHOICES, USERS_ROLES
    from django.core.validators import RegexValidator
    phone_regex = RegexValidator(regex=r'^9\d{8}$|^1\d{8}$',
                                 message=_("Phone number must start with 9 or 1 (no zeros) and includes 9 numbers."))
    username = models.CharField(
        verbose_name=_('User Name'),
        blank=False,
        null=False,
        max_length=350,
        unique=True

    )

    user_role = models.PositiveSmallIntegerField(choices=USERS_ROLES, default=4)
    full_name = models.CharField(
        verbose_name=_('Full Name'),
        max_length=350,
        blank=False,
        null=False
    )
    phone_number = models.CharField(
        verbose_name=_('Phone Number'),
        blank=False,
        null=False,
        max_length=100,
        unique=True
    )
    gender = models.CharField(
        verbose_name=_('Gender'),
        blank=False,
        null=False,
        max_length=10,
        choices=GENDER_CHOICES
    )
    email = models.EmailField(
        verbose_name=_('Email Address'),
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
    last_login = models.DateTimeField(auto_now=True, blank=True, null=True)
    registration_datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # role = models.PositiveIntegerField(verbose_name=_('User Role'),default=1)

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['password', 'email', 'full_name', 'gender',
                       'username']  # Email & Password are required by default.
    objects = UserAccountManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.full_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.full_name

    def __str__(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # return self.user_role == 3
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        # return self.user_role == 1
        return self.admin


class CreditCard(models.Model):
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        verbose_name=_('User')
    )
    card_name = models.CharField(
        verbose_name=('Card Name'),
        blank=False, null=False,
        default='',
        max_length=350
    )
    card_number = models.CharField(
        verbose_name=_('Card Number'),
        max_length=500,
        blank=False, null=False
    )
    card_ending_date = models.DateField(
        verbose_name=('Card Ending Date'),
        blank=False, null=False
    )
