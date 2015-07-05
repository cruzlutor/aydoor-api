# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_booking_ammount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='ammount',
            field=models.PositiveSmallIntegerField(max_length=2),
            preserve_default=True,
        ),
    ]
