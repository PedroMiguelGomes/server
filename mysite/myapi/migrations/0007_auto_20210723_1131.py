# Generated by Django 3.2.2 on 2021-07-23 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0006_auto_20210523_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=255)),
                ('toDo', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='progress',
            name='progress',
            field=models.IntegerField(),
        ),
    ]
