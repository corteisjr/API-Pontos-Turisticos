# Generated by Django 3.2.7 on 2021-09-10 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='aprovado',
            field=models.BooleanField(default=True),
        ),
    ]