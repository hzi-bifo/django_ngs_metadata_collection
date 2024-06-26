# Generated by Django 5.0.4 on 2024-04-10 17:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_sample_alias_sample_investigation_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_object_xml', models.TextField(blank=True, null=True)),
                ('submission_object_xml', models.TextField(blank=True, null=True)),
                ('receipt_xml', models.TextField(blank=True, null=True)),
                ('sample_accession_number', models.CharField(blank=True, max_length=100, null=True)),
                ('samea_accession_number', models.CharField(blank=True, max_length=100, null=True)),
                ('accession_status', models.CharField(blank=True, max_length=100, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.order')),
                ('samples', models.ManyToManyField(to='app.sample')),
            ],
        ),
    ]
