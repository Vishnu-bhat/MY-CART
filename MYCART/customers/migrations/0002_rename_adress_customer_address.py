# Generated by Django 5.0.6 on 2024-05-15 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='adress',
            new_name='address',
        ),
    ]