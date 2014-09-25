# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auchan', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drive',
            old_name='identifier',
            new_name='identifiant',
        ),
        migrations.RenameField(
            model_name='drive',
            old_name='name',
            new_name='ville',
        ),
    ]
