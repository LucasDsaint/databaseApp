# Generated by Django 2.2.17 on 2020-12-01 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='assunto',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='atendente',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='contatar',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_date',
            new_name='data',
        ),
        migrations.AddField(
            model_name='post',
            name='nome',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]