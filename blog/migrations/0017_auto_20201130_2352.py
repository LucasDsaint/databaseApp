# Generated by Django 2.2.17 on 2020-12-01 02:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0016_auto_20201130_2349'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Lista',
        ),
    ]
