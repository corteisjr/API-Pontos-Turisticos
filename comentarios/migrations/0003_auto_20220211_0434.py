# Generated by Django 3.0 on 2022-02-11 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_comentario_aprovado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
