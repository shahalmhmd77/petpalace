# Generated by Django 5.1.4 on 2025-01-24 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petpalaceapp', '0004_groomingappointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='product_images/')),
            ],
        ),
        migrations.DeleteModel(
            name='GroomingAppointment',
        ),
        migrations.AlterField(
            model_name='pet',
            name='contact',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_type',
            field=models.CharField(max_length=50),
        ),
    ]
