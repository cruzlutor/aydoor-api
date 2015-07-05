# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_advert_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='description',
            field=models.TextField(default='TOdo bien esto es una descripcion'),
            preserve_default=False,
        ),
    ]
