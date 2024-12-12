from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.company import Company
from user.models.user import User

class UserCompany(models.Model):
    """
    Usuario por Compañía.

    Representa la relación entre un usuario y una compañía, permitiendo gestionar
    el acceso de usuarios a múltiples compañías en el sistema.

    ¿Para qué sirve?:

    1. Gestión de permisos de usuarios por compañía.

    2. Control de acceso multiempresa para cada usuario.

    3. Seguimiento de actividades de usuarios por compañía.

    4. Configuración de preferencias específicas por usuario y compañía.

    5. Soporte para roles y responsabilidades diferentes en cada compañía.

    Creado por:
    @Claudio 

    Fecha: 27/10/2024
    """

    id_useco = models.BigAutoField(
        primary_key=True,
        verbose_name=_("ID de Usuario por Compañía"),
        help_text=_("Identificador único para la relación usuario-compañía.")
    )

    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='user_companies',
        verbose_name=_("Usuario"),
        help_text=_("Usuario asociado a la compañía.")
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        related_name='company_users',
        verbose_name=_("Compañía"),
        help_text=_("Compañía asociada al usuario.")
    )

    useco_active = models.BooleanField(
        default=True,
        verbose_name=_("Estado de la Relación"),
        help_text=_("Indica si la relación usuario-compañía está activa (True) o inactiva (False).")
    )

    class Meta:
        verbose_name = _("Usuario por Compañía")
        verbose_name_plural = _("Usuarios por Compañía")
        unique_together = ['user', 'company']

    def __str__(self):
        return f"{self.user.user_username} - {self.company.compa_name} ({self.id_useco})"

