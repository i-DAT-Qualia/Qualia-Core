# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QualiaUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('is_active', models.BooleanField(default=True)),
                ('is_beta', models.BooleanField(default=False)),
                ('level', models.IntegerField(default=1, choices=[(5, b'Admin'), (4, b'System Super'), (3, b'Org Super'), (2, b'Org User'), (1, b'User')])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
