# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_booking_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='ammount',
            field=models.CharField(default='5 horas', max_length=150),
            preserve_default=False,
        ),
    ]
