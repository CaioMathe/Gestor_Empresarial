# Generated by Django 4.0.5 on 2022-06-17 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_colaborador_id_colaborador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='id_colaborador',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
