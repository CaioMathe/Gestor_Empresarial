# Generated by Django 4.0.5 on 2022-06-18 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_colaborador_id_colaborador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='id_empresa_colab',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
