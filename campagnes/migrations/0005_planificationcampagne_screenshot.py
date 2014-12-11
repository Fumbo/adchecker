# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campagnes', '0004_auto_20141203_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='planificationcampagne',
            name='screenshot',
            field=models.ImageField(default=None, null=True, upload_to=b''),
            preserve_default=True,
        ),
    ]