# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auchan', '0004_drive_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drive',
            name='url',
        ),
    ]
