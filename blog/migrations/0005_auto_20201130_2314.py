# Generated by Django 2.2.17 on 2020-12-01 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201130_2304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='assunto',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_date',
            new_name='data',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='nome',
        ),
    ]
