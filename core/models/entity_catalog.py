from django.db import models
from django.utils.translation import gettext_lazy as _

class EntityCatalog(models.Model):
    """
    Catálogo de Entidades.
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

    # **NUEVOS CAMPOS**
    ENTIT_TYPE_CHOICES = [
        ('branch_office', 'Branch Office'),
        ('cost_center', 'Cost Center'),
    ]

    entit_type = models.CharField(
        max_length=50,
        choices=ENTIT_TYPE_CHOICES,
        verbose_name=_("Tipo de Entidad"),
        help_text=_("Tipo de entidad: Sucursal o Centro de Costos.")
    )

    company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,
        related_name="entities",
        verbose_name=_("Compañía"),
        help_text=_("Compañía a la que pertenece la entidad.")
    )

    class Meta:
        verbose_name = _("Catálogo de Entidad")
        verbose_name_plural = _("Catálogos de Entidades")

    def __str__(self):
        return f"{self.entit_name} ({self.entit_type})"
