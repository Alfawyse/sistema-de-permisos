from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.company import Company

class CostCenter(models.Model):
    """
    Centro de Costo.

    Un centro de costo representa una unidad organizacional dentro de una empresa
    que permite agrupar y controlar costos específicos.

    ¿Para qué sirve?:

    1. Gestión y control de costos por unidad organizativa.

    2. Seguimiento detallado de gastos y presupuestos por área.

    3. Análisis de rentabilidad por centro de responsabilidad.

    4. Facilitación de la toma de decisiones basada en costos.

    5. Implementación de estructuras jerárquicas para el control de costos.

    Creado por:
    @Claudio

    Fecha: 27/10/2024
    """

    id_cosce = models.BigAutoField(
        primary_key=True,
        verbose_name=_("ID del Centro de Costo"),
        help_text=_("Identificador único para el centro de costo.")
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        related_name='cost_centers',
        verbose_name=_("Compañía"),
        help_text=_("Compañía a la que pertenece este centro de costo.")
    )

    cosce_parent = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='children',
        verbose_name=_("Centro de Costo Padre"),
        help_text=_("Centro de costo superior en la jerarquía organizacional.")
    )

    cosce_code = models.CharField(
        verbose_name=_("Código"),
        help_text=_("Código único que identifica el centro de costo.")
    )

    cosce_name = models.CharField(
        verbose_name=_("Nombre"),
        help_text=_("Nombre descriptivo del centro de costo.")
    )

    cosce_description = models.TextField(
        blank=True,
        verbose_name=_("Descripción"),
        help_text=_("Descripción detallada del centro de costo y su propósito.")
    )

    cosce_budget = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0,
        verbose_name=_("Presupuesto"),
        help_text=_("Presupuesto asignado al centro de costo.")
    )

    cosce_level = models.PositiveSmallIntegerField(
        default=1,
        verbose_name=_("Nivel Jerárquico"),
        help_text=_("Nivel en la jerarquía de centros de costo (1 para nivel superior).")
    )

    cosce_active = models.BooleanField(
        default=True,
        verbose_name=_("Estado del Centro de Costo"),
        help_text=_("Indica si el centro de costo está activo (True) o inactivo (False).")
    )

    class Meta:
        verbose_name = _("Centro de Costo")
        verbose_name_plural = _("Centros de Costo")
        unique_together = ['company', 'cosce_code']

    def __str__(self):
        return f"{self.cosce_name} ({self.cosce_code}) [{self.id_cosce}]"




