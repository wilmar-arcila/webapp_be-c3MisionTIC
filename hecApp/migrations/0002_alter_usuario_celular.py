# Generated by Django 4.1.1 on 2022-09-16 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hecApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='celular',
            field=models.CharField(max_length=30, verbose_name='Celular'),
        ),
    ]
