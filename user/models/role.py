from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.company import Company

class Role(models.Model):
    """
    Rol.

    Un rol representa un conjunto de permisos y responsabilidades que pueden
    ser asignados a usuarios dentro de una compañía específica.

    ¿Para qué sirve?:

    1. Definición de niveles de acceso y permisos por compañía.

    2. Agrupación de funcionalidades y accesos para asignación eficiente.

    3. Control granular de las capacidades de los usuarios en el sistema.

    4. Simplificación de la gestión de permisos por grupos de usuarios.

    5. Estandarización de roles y responsabilidades dentro de cada compañía.

    Creado por:
    @Claudio

    Fecha: 27/10/2024
    """

    id_role = models.BigAutoField(
        primary_key=True,
        verbose_name=_("ID del Rol"),
        help_text=_("Identificador único para el rol.")
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        related_name='company_roles',
        verbose_name=_("Compañía"),
        help_text=_("Compañía a la que pertenece este rol.")
    )

    role_name = models.CharField(
        verbose_name=_("Nombre del Rol"),
        help_text=_("Nombre descriptivo del rol.")
    )

    role_description = models.TextField(
        blank=True,
        verbose_name=_("Descripción"),
        help_text=_("Descripción detallada del rol y sus responsabilidades.")
    )

    role_active = models.BooleanField(
        default=True,
        verbose_name=_("Estado del Rol"),
        help_text=_("Indica si el rol está activo (True) o inactivo (False).")
    )

    class Meta:
        verbose_name = _("Rol")
        verbose_name_plural = _("Roles")
        unique_together = ['company', 'role_code']

    def __str__(self):
        return f"{self.role_name} - {self.company.compa_name} ({self.id_role})"
