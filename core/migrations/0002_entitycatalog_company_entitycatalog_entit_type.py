# Generated by Django 5.1.4 on 2024-12-16 01:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entitycatalog',
            name='company',
            field=models.ForeignKey(default=1, help_text='Compañía a la que pertenece la entidad.', on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='core.company', verbose_name='Compañía'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entitycatalog',
            name='entit_type',
            field=models.CharField(choices=[('branch_office', 'Branch Office'), ('cost_center', 'Cost Center')], default=1, help_text='Tipo de entidad: Sucursal o Centro de Costos.', max_length=50, verbose_name='Tipo de Entidad'),
            preserve_default=False,
        ),
    ]