# Generated by Django 3.0.4 on 2020-06-03 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partage_repas', '0018_profil_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar'),
        ),
    ]
