# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_infopack_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infopack',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
