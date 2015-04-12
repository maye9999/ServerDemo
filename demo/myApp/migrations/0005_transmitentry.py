# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myApp', '0004_auto_20141209_0042'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransmitEntry',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('flow', models.BigIntegerField()),
                ('user_from', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='entries_from')),
                ('user_to', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='entries_to')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
