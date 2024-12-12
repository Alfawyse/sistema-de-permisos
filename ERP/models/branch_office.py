from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.company import Company

class BranchOffice(models.Model):
    """
    Sucursal.

    Una sucursal representa un establecimiento físico o punto de operación 
    que pertenece a una compañía específica.

    ¿Para qué sirve?:

    1. Gestión y control de múltiples ubicaciones de una misma empresa.

    2. Organización de operaciones por punto de venta o servicio.

    3. Seguimiento y análisis de desempeño por sucursal.

    4. Asignación y control de recursos específicos por ubicación.

    5. Facilitar la gestión descentralizada de operaciones empresariales.

    Creado por:
    @Claude Assistant

    Fecha: 27/10/2024
    """

    id_broff = models.BigAutoField(
        primary_key=True,
        verbose_name=_("ID de Sucursal"),
        help_text=_("Identificador único para la sucursal.")
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        related_name='branch_offices',
        verbose_name=_("Compañía"),
        help_text=_("Compañía a la que pertenece esta sucursal.")
    )

    broff_name = models.CharField(
        verbose_name=_("Nombre de Sucursal"),
        help_text=_("Nombre descriptivo de la sucursal.")
    )

    broff_code = models.CharField(
        verbose_name=_("Código de Sucursal"),
        help_text=_("Código único que identifica la sucursal dentro de la empresa.")
    )

    broff_address = models.CharField(
        verbose_name=_("Dirección"),
        help_text=_("Dirección física de la sucursal.")
    )

    broff_city = models.CharField(
        verbose_name=_("Ciudad"),
        help_text=_("Ciudad donde está ubicada la sucursal.")
    )

    broff_state = models.CharField(
        verbose_name=_("Departamento/Estado"),
        help_text=_("Departamento o estado donde está ubicada la sucursal.")
    )

    broff_country = models.CharField(
        verbose_name=_("País"),
        help_text=_("País donde está ubicada la sucursal.")
    )

    broff_phone = models.CharField(
        verbose_name=_("Teléfono"),
        help_text=_("Número de teléfono de la sucursal.")
    )

    broff_email = models.EmailField(
        verbose_name=_("Correo Electrónico"),
        help_text=_("Dirección de correo electrónico de la sucursal.")
    )

    broff_active = models.BooleanField(
        default=True,
        verbose_name=_("Estado de la Sucursal"),
        help_text=_("Indica si la sucursal está activa (True) o inactiva (False).")
    )

    class Meta:
        verbose_name = _("Sucursal")
        verbose_name_plural = _("Sucursales")
        unique_together = ['company', 'broff_code']

    def __str__(self):
        return f"{self.broff_name} - {self.company.compa_name} ({self.id_broff})"

    def clean(self):
        self.broff_name = self.broff_name.title()
        self.broff_code = self.broff_code.upper()
        self.broff_city = self.broff_city.title()
        self.broff_state = self.broff_state.title()
        self.broff_country = self.broff_country.title()
        super().clean()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)