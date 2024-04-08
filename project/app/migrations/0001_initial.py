# Generated by Django 5.0.4 on 2024-04-07 11:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('billing_address', models.TextField(blank=True, null=True)),
                ('ag_and_hzi', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('quote_no', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('data_delivery', models.CharField(blank=True, max_length=100, null=True)),
                ('signature', models.CharField(blank=True, max_length=100, null=True)),
                ('experiment_title', models.CharField(blank=True, max_length=100, null=True)),
                ('dna', models.CharField(blank=True, max_length=20, null=True)),
                ('rna', models.CharField(blank=True, max_length=20, null=True)),
                ('library', models.CharField(blank=True, max_length=20, null=True)),
                ('method', models.CharField(blank=True, max_length=100, null=True)),
                ('buffer', models.CharField(blank=True, max_length=100, null=True)),
                ('organism', models.CharField(blank=True, max_length=100, null=True)),
                ('isolated_from', models.CharField(blank=True, max_length=100, null=True)),
                ('isolation_method', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_name', models.CharField(blank=True, max_length=100, null=True)),
                ('concentration', models.CharField(blank=True, max_length=100, null=True)),
                ('volume', models.CharField(blank=True, max_length=100, null=True)),
                ('ratio_260_280', models.CharField(blank=True, max_length=100, null=True)),
                ('ratio_260_230', models.CharField(blank=True, max_length=100, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('internal_id', models.DateTimeField(auto_now_add=True)),
                ('metadata_type', models.CharField(blank=True, max_length=100, null=True)),
                ('metadata_a', models.CharField(blank=True, max_length=100, null=True)),
                ('metadata_b', models.CharField(blank=True, max_length=100, null=True)),
                ('metadata_c', models.CharField(blank=True, max_length=100, null=True)),
                ('metadata_d', models.CharField(blank=True, max_length=100, null=True)),
                ('metadata_e', models.CharField(blank=True, max_length=100, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.order')),
            ],
        ),
    ]