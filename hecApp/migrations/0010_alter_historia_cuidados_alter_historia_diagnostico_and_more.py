# Generated by Django 4.1.1 on 2022-09-23 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hecApp', '0009_alter_paciente_familiar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historia',
            name='cuidados',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='historia',
            name='diagnostico',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='historia',
            name='f_cardiaca',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='historia',
            name='f_respiratoria',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='historia',
            name='glicemias',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='historia',
            name='oximetria',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='historia',
            name='presion_arterial',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='historia',
            name='temperatura',
            field=models.JSONField(null=True),
        ),
    ]
