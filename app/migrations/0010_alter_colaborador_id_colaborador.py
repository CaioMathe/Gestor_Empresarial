# Generated by Django 4.0.5 on 2022-06-17 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_colaborador_id_colaborador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='id_colaborador',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
