# Generated by Django 3.0 on 2022-02-11 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0002_rename_endereco_enderecos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enderecos',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
