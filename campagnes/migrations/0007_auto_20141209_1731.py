# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campagnes', '0006_rayon_identifiant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planificationcampagne',
            name='screenshot',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
