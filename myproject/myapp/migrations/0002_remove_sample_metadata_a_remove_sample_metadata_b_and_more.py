# Generated by Django 5.0.4 on 2024-04-07 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='metadata_a',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='metadata_b',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='metadata_c',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='metadata_d',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='metadata_e',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='metadata_type',
        ),
    ]
