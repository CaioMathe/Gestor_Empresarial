# Generated by Django 4.0.5 on 2022-06-17 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_empresas_id_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='id_colaborador',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
