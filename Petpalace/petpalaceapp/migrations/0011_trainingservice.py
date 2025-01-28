# Generated by Django 5.1.4 on 2025-01-27 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petpalaceapp', '0010_groomingservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='trainingservice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('pet_name', models.CharField(max_length=255)),
                ('pet_age', models.IntegerField()),
                ('message', models.TextField(blank=True)),
            ],
        ),
    ]
