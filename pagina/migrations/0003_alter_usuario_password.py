# Generated by Django 4.0.2 on 2022-04-12 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0002_usuario_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
