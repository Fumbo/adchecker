# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campagnes', '0002_auto_20141002_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campagne',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=50)),
                ('annonceur', models.CharField(max_length=50)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rayon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=50)),
                ('parent', models.ForeignKey(default=None, blank=True, to='campagnes.Rayon')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='enseigne',
            name='nom',
            field=models.CharField(max_length=50),
        ),
    ]
