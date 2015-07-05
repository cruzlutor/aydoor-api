# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_advert_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='state',
            field=models.PositiveSmallIntegerField(default=1, max_length=1, choices=[(1, b'REQUEST'), (2, b'ACCPETED'), (3, b'CANCELED'), (4, b'FINISHED')]),
            preserve_default=True,
        ),
    ]
