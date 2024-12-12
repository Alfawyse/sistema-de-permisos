from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.entity_catalog import EntityCatalog
from user.models.permission import Permission
from user.models.user_company import UserCompany

class PermiUser(models.Model):
    """
    Permiso de Usuario.

    Representa los permisos específicos asignados a un usuario para una 
    entidad particular dentro de una compañía.

    ¿Para qué sirve?:

    1. Asignación de permisos específicos por usuario y entidad.

    2. Control granular de accesos a nivel de usuario-compañía.

    3. Personalización de capacidades por entidad del sistema.

    4. Gestión detallada de privilegios por usuario.

    5. Implementación de políticas de seguridad específicas por entidad.

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
    peusr_include = models.BooleanField(
        default=True,
        verbose_name=_("Incluir Permiso"),
        help_text=_("Indica si el permiso se incluye (True) o se excluye (False) para el usuario.")
    )

    class Meta:
        verbose_name = _("Permiso de Usuario")
        verbose_name_plural = _("Permisos de Usuario")
        unique_together = ['usercompany', 'permission', 'entitycatal']
