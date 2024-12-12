from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models.entity_catalog import EntityCatalog
from user.models.permission import Permission
from user.models.role import Role

class PermiRole(models.Model):
    """
    Permiso por Rol.

    Representa los permisos específicos asignados a un rol para una 
    entidad particular dentro del sistema.

    ¿Para qué sirve?:

    1. Asignación de permisos específicos por rol y entidad.

    2. Control granular de accesos a nivel de rol.

    3. Personalización de capacidades por entidad del sistema.

    4. Gestión detallada de privilegios por rol.

    5. Implementación de políticas de seguridad específicas por rol y entidad.

    Creado por:
    @Claudio

    Fecha: 27/10/2024
    """

    id_perol = models.BigAutoField(
        primary_key=True,
        verbose_name=_("ID de Permiso de Rol"),
        help_text=_("Identificador único para el permiso de rol.")
    )

    role = models.ForeignKey(
        Role,
        on_delete=models.PROTECT,
        related_name='role_permissions',
        verbose_name=_("Rol"),
        help_text=_("Rol al que se asigna el permiso.")
    )

    permission = models.ForeignKey(
        Permission,
        on_delete=models.PROTECT,
        related_name='permission_roles',
        verbose_name=_("Permiso"),
        help_text=_("Permiso asignado al rol.")
    )

    entitycatalog = models.ForeignKey(
        EntityCatalog,
        on_delete=models.PROTECT,
        related_name='entity_role_permissions',
        verbose_name=_("Entidad"),
        help_text=_("Entidad sobre la que se aplica el permiso.")
    )



    perol_include = models.BooleanField(
        default=True,
        verbose_name=_("Incluir Permiso"),
        help_text=_("Indica si el permiso se incluye (True) o se excluye (False) para el rol.")
    )

    class Meta:
        verbose_name = _("Permiso de Rol")
        verbose_name_plural = _("Permisos de Rol")
        unique_together = ['role', 'permission', 'entitycatalog', 'perol_record']

