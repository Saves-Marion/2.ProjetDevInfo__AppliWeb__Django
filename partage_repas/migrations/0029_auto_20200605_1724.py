# Generated by Django 3.0.4 on 2020-06-05 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partage_repas', '0028_auto_20200605_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repas',
            name='allergene',
            field=models.CharField(blank=True, choices=[('Aucun', 'Aucun'), ('Lait', 'Lait'), ('Oeufs', 'Oeufs'), ('Crustacé-Mollusque', 'Crustacé-Mollusque'), ('Noix', 'Noix')], max_length=100, null=True),
        ),
    ]
