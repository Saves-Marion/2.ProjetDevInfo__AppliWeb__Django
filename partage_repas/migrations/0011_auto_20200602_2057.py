# Generated by Django 3.0.4 on 2020-06-02 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partage_repas', '0010_auto_20200602_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='repas',
            name='participants',
            field=models.ManyToManyField(to='partage_repas.Profil'),
        ),
        migrations.DeleteModel(
            name='Inscription',
        ),
    ]
