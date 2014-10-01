# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drive',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ville', models.CharField(max_length=30)),
                ('identifiant', models.PositiveSmallIntegerField(unique=True)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['enseigne'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Enseigne',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=100)),
                ('url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='drive',
            name='enseigne',
            field=models.ForeignKey(to='campagnes.Enseigne'),
            preserve_default=True,
        ),
    ]
