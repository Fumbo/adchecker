# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campagnes', '0003_auto_20141203_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rayon',
            name='magasin',
        ),
        migrations.AddField(
            model_name='planificationcampagne',
            name='magasin',
            field=models.ForeignKey(default=1, to='campagnes.Magasin'),
            preserve_default=False,
        ),
    ]
