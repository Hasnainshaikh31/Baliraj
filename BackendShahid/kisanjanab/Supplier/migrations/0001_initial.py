# Generated by Django 3.0.6 on 2020-05-14 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=150)),
                ('middleName', models.CharField(max_length=150)),
                ('lastName', models.CharField(max_length=150)),
                ('phoneNumber', models.DecimalField(blank=True, decimal_places=0, max_digits=10)),
                ('mobileNumber', models.DecimalField(decimal_places=0, max_digits=10)),
                ('email', models.EmailField(max_length=255)),
                ('emailOptional', models.EmailField(blank=True, max_length=255)),
                ('address', models.TextField()),
                ('areaStreet', models.TextField()),
                ('city', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('taluka', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('pinCode', models.DecimalField(decimal_places=0, max_digits=6)),
            ],
        ),
    ]
