# Generated by Django 3.2.2 on 2021-07-23 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0008_auto_20210723_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='number',
            new_name='completed',
        ),
    ]
