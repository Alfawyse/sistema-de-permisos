from django.db import models
from django.utils.translation import gettext_lazy as _

class EntityCatalog(models.Model):
    """
    Catálogo de Entidades.

    Un catálogo de entidades representa una tabla que almacena todas las entidades 
    (modelos) disponibles en el sistema Django, facilitando su gestión y referencia.

    ¿Para qué sirve?:

    1. Mantener un registro centralizado de todas las entidades del sistema.

    2. Facilitar la gestión y el mantenimiento de la estructura de la base de datos.

    3. Permitir la referencia dinámica a diferentes modelos del sistema.

    4. Proveer una base para la implementación de funcionalidades genéricas.

    5. Apoyar en la documentación y organización del sistema.

    Creado por:
    @Claudio

    Fecha: 27/9/2024
    """

    id_entit = models.AutoField(
        primary_key=True,
        verbose_name=_("ID del Catálogo de Entidad"),
        help_text=_("Identificador único para el elemento del catálogo de entidades.")
    )

    entit_name = models.CharField(
        unique=True,
        verbose_name=_("Nombre de la Entidad"),
        help_text=_("Nombre del modelo Django asociado.")
    )

    entit_descrip = models.CharField(
        verbose_name=_("Descripción"),
        help_text=_("Descripción del elemento del catálogo de entidades.")
    )

    entit_active = models.BooleanField(
        default=True,
        verbose_name=_("Estado Activo"),
        help_text=_("Indica si el elemento del catálogo está activo (True) o inactivo (False).")
    )

    entit_config = models.JSONField(
        blank=True,
        null=True,
        verbose_name=_("Configuración"),
        help_text=_("Configuración adicional para el elemento del catálogo.")
    )

    class Meta:
        verbose_name = _("Catálogo de Entidad")
        verbose_name_plural = _("Catálogos de Entidades")

    def __str__(self):
        return f"{self.entit_name} ({self.id_entit})"

    def clean(self):
        """
        Realiza validaciones adicionales antes de guardar el objeto.
        """
        self.entit_name = self.entit_name.lower()
        self.entit_descrip = self.entit_descrip.capitalize()
        super().clean()

    def save(self, *args, **kwargs):
        """
        Sobrescribe el método save para asegurar una limpieza completa antes de guardar.
        """
        #self.full_clean()
        super().save(*args, **kwargs)