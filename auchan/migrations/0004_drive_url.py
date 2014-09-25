# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auchan', '0003_drive_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='drive',
            name='url',
            field=models.URLField(default=b'http://auchandrive.fr/drive/'),
            preserve_default=True,
        ),
    ]
