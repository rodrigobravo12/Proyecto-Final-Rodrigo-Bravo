# Generated by Django 5.0.2 on 2024-03-03 20:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0004_remove_equipo_fechaentrega'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='fechaInscripcion',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
