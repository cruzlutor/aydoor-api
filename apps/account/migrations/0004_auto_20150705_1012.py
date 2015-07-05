# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.account.utils


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20150705_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(null=True, upload_to=apps.account.utils.upload_avatar, blank=True),
            preserve_default=True,
        ),
    ]
