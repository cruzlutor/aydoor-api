# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20150705_0127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='user_service',
            new_name='advert',
        ),
    ]
