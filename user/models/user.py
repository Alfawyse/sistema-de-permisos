from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, user_username, user_email, password=None, **extra_fields):
        if not user_email:
            raise ValueError("El correo electrónico es obligatorio")
        user_email = self.normalize_email(user_email)
        user = self.model(user_username=user_username, user_email=user_email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_username, user_email, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(user_username, user_email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    id_user = models.BigAutoField(primary_key=True)
    user_username = models.CharField(max_length=150, unique=True, verbose_name=_("Nombre de Usuario"))
    user_email = models.EmailField(unique=True, verbose_name=_("Correo Electrónico"))
    user_phone = models.CharField(max_length=20, blank=True, verbose_name=_("Teléfono"))
    user_is_active = models.BooleanField(default=True, verbose_name=_("Usuario Activo"))
    user_is_admin = models.BooleanField(default=False, verbose_name=_("Usuario Administrador"))

    objects = UserManager()

    USERNAME_FIELD = 'user_username'
    REQUIRED_FIELDS = ['user_email']

    class Meta:
        verbose_name = _("Usuario")
        verbose_name_plural = _("Usuarios")

    def __str__(self):
        return f"{self.user_username} ({self.user_email})"

    @property
    def is_staff(self):
        return self.user_is_admin

