# Generated by Django 2.2.17 on 2020-12-01 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_post_nome'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='nome',
            new_name='contatar',
        ),
    ]
