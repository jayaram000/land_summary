# Generated by Django 5.2.1 on 2025-05-25 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Land',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parcel_id', models.CharField(max_length=100)),
                ('plot_number', models.CharField(max_length=100)),
                ('owner_name', models.CharField(max_length=150)),
                ('location', models.TextField()),
                ('area', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
