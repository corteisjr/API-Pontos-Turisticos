# Generated by Django 3.2.7 on 2021-09-12 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avaliacao',
            old_name='user',
            new_name='usuario',
        ),
    ]
