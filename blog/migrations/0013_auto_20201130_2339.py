# Generated by Django 2.2.17 on 2020-12-01 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20201130_2337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='nome',
        ),
    ]
