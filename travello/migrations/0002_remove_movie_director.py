# Generated by Django 3.2 on 2021-05-18 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
    ]
