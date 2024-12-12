from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models.entity_catalog import EntityCatalog
from user.models.permission import Permission
from user.models.user_company import UserCompany

class PermiUserRecord(models.Model):
    """
    Permiso de Usuario con Registro.

    Representa los permisos específicos asignados a un usuario para una 
    entidad particular y un registro específico dentro de una compañía.

    ¿Para qué sirve?:

    1. Asignación de permisos específicos por usuario y entidad a nivel de registro.

    2. Control granular de accesos a nivel de usuario-compañía y registro.

    3. Personalización de capacidades por entidad y registro del sistema.

    4. Gestión detallada de privilegios por usuario a nivel de registro.

    5. Implementación de políticas de seguridad específicas por entidad y registro.

    Creado por:
    @Claudio

    Fecha: 27/10/2024
    """

    id_peusr = models.BigAutoField(
        primary_key=True,
        verbose_name=_("ID de Permiso de Usuario"),
        help_text=_("Identificador único para el permiso de usuario.")
    )

    usercompany = models.ForeignKey(
        UserCompany,
        on_delete=models.PROTECT,
        related_name='user_permissions',
        verbose_name=_("Usuario por Compañía"),
        help_text=_("Relación usuario-compañía a la que se asigna el permiso.")
    )

    permission = models.ForeignKey(
        Permission,
        on_delete=models.PROTECT,
        related_name='permission_users',
        verbose_name=_("Permiso"),
        help_text=_("Permiso asignado al usuario.")
    )

    entitycatalog = models.ForeignKey(
        EntityCatalog,
        on_delete=models.PROTECT,
        related_name='entity_permissions',
        verbose_name=_("Entidad"),
        help_text=_("Entidad sobre la que se aplica el permiso.")
    )

    peusr_record = models.BigIntegerField(
        verbose_name=_("ID del Registro"),
        help_text=_("Identificador del registro específico de la entidad al que aplica el permiso.")
    )

    peusr_include = models.BooleanField(
        default=True,
        verbose_name=_("Incluir Permiso"),
        help_text=_("Indica si el permiso se incluye (True) o se excluye (False) para el usuario.")
    )

    class Meta:
        verbose_name = _("Permiso de Usuario por Registro")
        verbose_name_plural = _("Permisos de Usuario por Registro")
        unique_together = ['usercompany', 'permission', 'entitycatalog', 'peusr_record']

    def __str__(self):
        include_status = "incluido" if self.peusr_include else "excluido"
        return f"{self.usercompany.user.user_username} - {self.entitycatalog.entit_name}[{self.peusr_record}] - {self.permission.permi_name} ({include_status}) [{self.id_peusr}]"

    def clean(self):
        super().clean()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)