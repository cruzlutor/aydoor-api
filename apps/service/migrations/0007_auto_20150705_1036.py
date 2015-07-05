# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_auto_20150705_1028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='ammount',
            new_name='amount',
        ),
    ]
