# Generated by Django 3.0.4 on 2020-06-01 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partage_repas', '0004_auto_20200601_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='repas',
            name='nombre_d_inscrit',
            field=models.TextField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='repas',
            name='nombre_participant',
            field=models.TextField(null=True),
        ),
    ]
