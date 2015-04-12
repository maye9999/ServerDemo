# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='infopack',
            name='uuid',
            field=models.CharField(max_length=100, default=1),
            preserve_default=False,
        ),
    ]
