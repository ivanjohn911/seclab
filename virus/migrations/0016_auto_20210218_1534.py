# Generated by Django 3.0.5 on 2021-02-18 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('virus', '0015_auto_20210218_1110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='jobnum',
            new_name='username',
        ),
    ]
