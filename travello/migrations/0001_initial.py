# Generated by Django 3.2 on 2021-05-18 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('year', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('year', models.IntegerField()),
                ('genre', models.TextField(choices=[('Action', 'Action'), ('Cartoon', 'Cartoon'), ('Humor', 'Humor'), ('Thriller', 'Thriller')], default=0)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travello.director', unique=True)),
            ],
        ),
    ]
