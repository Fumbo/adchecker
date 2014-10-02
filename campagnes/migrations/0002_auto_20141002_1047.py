# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campagnes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Magasin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ville', models.CharField(max_length=30)),
                ('identifiant', models.PositiveSmallIntegerField(unique=True)),
                ('status', models.BooleanField(default=False)),
                ('enseigne', models.ForeignKey(to='campagnes.Enseigne')),
            ],
            options={
                'ordering': ['enseigne'],
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='drive',
            name='enseigne',
        ),
        migrations.DeleteModel(
            name='Drive',
        ),
    ]
