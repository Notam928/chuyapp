# Generated by Django 3.2.6 on 2023-10-09 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_observation_plaintes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='poids',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
    ]
