# Generated by Django 3.0.6 on 2020-05-19 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0004_auto_20200519_1321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='pinCode',
            new_name='pincode',
        ),
    ]