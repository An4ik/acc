# Generated by Django 2.1.1 on 2018-09-20 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('fuel_tank', models.PositiveIntegerField(verbose_name='fuel tank')),
                ('consumption', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='consumption')),
                ('passengers', models.IntegerField(default=0, verbose_name='passengers')),
            ],
        ),
    ]
