# Generated by Django 3.0 on 2022-02-11 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0003_auto_20220211_0434'),
        ('pontos_turisticos', '0008_auto_20220211_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='enderecos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='endereco.Enderecos'),
        ),
    ]