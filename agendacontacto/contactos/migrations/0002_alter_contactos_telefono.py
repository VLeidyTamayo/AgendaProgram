# Generated by Django 5.1 on 2024-08-15 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactos',
            name='telefono',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
