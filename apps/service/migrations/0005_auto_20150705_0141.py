# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0004_auto_20150705_0139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('booking', models.ForeignKey(to='service.Booking')),
                ('service', models.ForeignKey(related_name='service_advert', to='service.Service')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='userservice',
            name='booking',
        ),
        migrations.RemoveField(
            model_name='userservice',
            name='service',
        ),
        migrations.RemoveField(
            model_name='userservice',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserService',
        ),
        migrations.AlterField(
            model_name='service',
            name='advert',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, through='service.Advert', blank=True),
            preserve_default=True,
        ),
    ]
