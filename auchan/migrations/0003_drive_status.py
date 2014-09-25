# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auchan', '0002_auto_20140925_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='drive',
            name='status',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
