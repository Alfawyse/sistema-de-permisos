from django.db import models
from django.utils.translation import gettext_lazy as _

class Company(models.Model):
    """
    Compañía.

    Una compañía representa una entidad empresarial con sus datos de identificación,
    ubicación y características principales dentro del sistema ERP.

    ¿Para qué sirve?:

    1. Gestión centralizada de la información básica de las empresas en el sistema.

    2. Soporte para operaciones comerciales y administrativas específicas de cada empresa.

    3. Cumplimiento de requisitos legales y fiscales relacionados con la identificación empresarial.

    4. Base para la configuración de parámetros y políticas específicas de cada empresa.

    5. Facilitar la gestión multi-empresa dentro del sistema ERP.

    Creado por:
    @Claudio

    Fecha: 27/9/2024
    """

    id_compa = models.BigAutoField(
        primary_key=True,
        verbose_name=_("ID de Compañía"),
        help_text=_("Identificador único para la compañía.")
    )

    compa_name = models.CharField(
        verbose_name=_("Razón Social"),
        help_text=_("Nombre legal completo de la compañía.")
    )

    compa_tradename = models.CharField(
        verbose_name=_("Nombre Comercial"),
        help_text=_("Nombre comercial o marca de la compañía.")
    )

    compa_doctype = models.CharField(
        max_length=2,
        choices=[
            ('NI', _('NIT')),
            ('CC', _('Cédula de Ciudadanía')),
            ('CE', _('Cédula de Extranjería')),
            ('PP', _('Pasaporte')),
            ('OT', _('Otro'))
        ],
        verbose_name=_("Tipo de Documento"),
        help_text=_("Tipo de documento de identificación de la compañía.")
    )

    compa_docnum = models.CharField(
        verbose_name=_("Número de Documento"),
        help_text=_("Número de identificación fiscal o documento legal de la compañía.")
    )

    compa_address = models.CharField(
        verbose_name=_("Dirección"),
        help_text=_("Dirección física de la compañía.")
    )

    compa_city = models.CharField(
        verbose_name=_("Ciudad"),
        help_text=_("Ciudad donde está ubicada la compañía.")
    )

    compa_state = models.CharField(
        verbose_name=_("Departamento/Estado"),
        help_text=_("Departamento o estado donde está ubicada la compañía.")
    )

    compa_country = models.CharField(
        verbose_name=_("País"),
        help_text=_("País donde está ubicada la compañía.")
    )

    compa_industry = models.CharField(
        verbose_name=_("Industria"),
        help_text=_("Sector industrial al que pertenece la compañía.")
    )

    compa_phone = models.CharField(
        verbose_name=_("Teléfono"),
        help_text=_("Número de teléfono principal de la compañía.")
    )

    compa_email = models.EmailField(
        verbose_name=_("Correo Electrónico"),
        help_text=_("Dirección de correo electrónico principal de la compañía.")
    )

    compa_website = models.URLField(
        blank=True,
        verbose_name=_("Sitio Web"),
        help_text=_("Sitio web oficial de la compañía.")
    )

    compa_logo = models.ImageField(
        blank=True,
        verbose_name=_("Logo"),
        help_text=_("Logo oficial de la compañía.")
    )

    compa_active = models.BooleanField(
        default=True,
        verbose_name=_("Estado de la Compañía"),
        help_text=_("Indica si la compañía está activa (True) o inactiva (False).")
    )

    class Meta:
        verbose_name = _("Compañía")
        verbose_name_plural = _("Compañías")

    def __str__(self):
        return f"{self.compa_name} ({self.id_compa})"

    def clean(self):
        self.compa_name = self.compa_name.title()
        self.compa_tradename = self.compa_tradename.title()
        self.compa_docnum = self.compa_docnum.upper()
        self.compa_city = self.compa_city.title()
        self.compa_state = self.compa_state.title()
        self.compa_country = self.compa_country.title()
        self.compa_industry = self.compa_industry.title()
        super().clean()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)