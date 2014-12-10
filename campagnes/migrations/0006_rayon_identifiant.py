# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campagnes', '0005_planificationcampagne_screenshot'),
    ]

    operations = [
        migrations.AddField(
            model_name='rayon',
            name='identifiant',
            field=models.CharField(default='Boissons-Cave-R41358', max_length=50),
            preserve_default=False,
        ),
    ]
