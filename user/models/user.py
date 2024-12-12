from django.db import models
from django.utils.translation import gettext_lazy as _

class User(models.Model):
    """
    Usuario.

    Un usuario representa una persona que interactúa con el sistema,
    con sus credenciales y datos básicos de acceso.

    ¿Para qué sirve?:

    1. Gestión de acceso y autenticación en el sistema.

    2. Almacenamiento de información básica de los usuarios.

    3. Control de estados y permisos de usuarios.

    4. Seguimiento de actividad y auditoría de usuarios.

    5. Base para la personalización de la experiencia de usuario.

    Creado por:
    @Claudio

    Fecha: 27/10/2024
    """

    id_user = models.BigAutoField(
        primary_key=True,
        verbose_name=_("ID de Usuario"),
        help_text=_("Identificador único para el usuario.")
    )

    user_username = models.CharField(
        unique=True,
        verbose_name=_("Nombre de Usuario"),
        help_text=_("Nombre de usuario para iniciar sesión.")
    )

    user_password = models.CharField(
        verbose_name=_("Contraseña"),
        help_text=_("Contraseña encriptada del usuario.")
    )

    user_email = models.EmailField(
        unique=True,
        verbose_name=_("Correo Electrónico"),
        help_text=_("Dirección de correo electrónico del usuario.")
    )

    user_phone = models.CharField(
        blank=True,
        verbose_name=_("Teléfono"),
        help_text=_("Número de teléfono del usuario.")
    )

    user_is_admin = models.BooleanField(
        default=False,
        verbose_name=_("Usuario Administrador"),
        help_text=_("Indica si el usuario es Administrador (True) o normal (False).")
    )

    user_is_active = models.BooleanField(
        default=True,
        verbose_name=_("Usuario Activo"),
        help_text=_("Indica si el usuario está activo (True) o inactivo (False).")
    )


    class Meta:
        verbose_name = _("Usuario")
        verbose_name_plural = _("Usuarios")

    def __str__(self):
        return f"{self.user_first_name} {self.user_last_name} ({self.user_username})"

