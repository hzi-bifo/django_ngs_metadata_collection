# Generated by Django 5.0.4 on 2024-04-08 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_order_contact_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='mixs_metadata',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
