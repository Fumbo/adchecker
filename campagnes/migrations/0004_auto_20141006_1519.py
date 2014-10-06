# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campagnes', '0003_auto_20141006_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rayon',
            name='parent',
            field=models.ForeignKey(blank=True, to='campagnes.Rayon', null=True),
        ),
    ]
