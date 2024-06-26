# Generated by Django 5.0.4 on 2024-04-07 23:29

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_sample_mixs_metadata_standard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='contact_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='order',
            name='isolation_method',
            field=models.CharField(blank=True, choices=[('method1', 'Method 1'), ('method2', 'Method 2'), ('other', 'Other')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='library',
            field=models.CharField(blank=True, choices=[('choice1', 'Choice 1'), ('choice2', 'Choice 2'), ('other', 'Other')], max_length=20, null=True),
        ),
    ]
