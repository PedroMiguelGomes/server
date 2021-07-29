# Generated by Django 3.2.2 on 2021-05-23 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0005_question_completed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='completed',
        ),
    ]
