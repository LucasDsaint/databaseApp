# Generated by Django 2.2.17 on 2020-12-01 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20201130_2316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='assunto',
        ),
    ]
