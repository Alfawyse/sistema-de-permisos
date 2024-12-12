from django.db import models
from django.utils.translation import gettext_lazy as _

class Permission(models.Model):
    """
    Permiso.

    Un permiso representa los diferentes niveles de acceso y operaciones
    que pueden realizarse sobre una entidad del sistema.

    ¿Para qué sirve?:

    1. Control granular de acciones sobre entidades del sistema.

    2. Definición de permisos específicos para operaciones CRUD.

    3. Gestión de capacidades de importación y exportación de datos.

    4. Implementación de políticas de seguridad y acceso.

    5. Configuración flexible de permisos por funcionalidad.

    Creado por:
    @Claudio

    Fecha: 27/10/2024
    """

    id_permi = models.BigAutoField(
        primary_key=True,
        verbose_name=_("ID del Permiso"),
        help_text=_("Identificador único para el permiso.")
    )

    name = models.CharField(
        verbose_name=_("Nombre del Permiso"),
        help_text=_("Nombre descriptivo del permiso.")
    )


    description = models.TextField(
        blank=True,
        verbose_name=_("Descripción"),
        help_text=_("Descripción detallada del permiso y su propósito.")
    )

    can_create = models.BooleanField(
        default=False,
        verbose_name=_("Puede Crear"),
        help_text=_("Permite crear nuevos registros.")
    )

    can_read = models.BooleanField(
        default=False,
        verbose_name=_("Puede Leer"),
        help_text=_("Permite ver registros existentes.")
    )

    can_update = models.BooleanField(
        default=False,
        verbose_name=_("Puede Actualizar"),
        help_text=_("Permite modificar registros existentes.")
    )

    can_delete = models.BooleanField(
        default=False,
        verbose_name=_("Puede Eliminar"),
        help_text=_("Permite eliminar registros existentes.")
    )

    can_import = models.BooleanField(
        default=False,
        verbose_name=_("Puede Importar"),
        help_text=_("Permite importar datos masivamente.")
    )

    can_export = models.BooleanField(
        default=False,
        verbose_name=_("Puede Exportar"),
        help_text=_("Permite exportar datos del sistema.")
        )
    class Meta:
        verbose_name = _("Permiso")
        verbose_name_plural = _("Permisos")


    def __str__(self):
        return f"{self.name}  [{self.id_permi}]"

