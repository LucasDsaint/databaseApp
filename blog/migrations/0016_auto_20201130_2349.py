# Generated by Django 2.2.17 on 2020-12-01 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_remove_post_created_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='data',
            new_name='horário',
        ),
    ]
