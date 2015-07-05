# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0002_service_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('booking', models.ForeignKey(to='service.Booking')),
                ('service', models.ForeignKey(to='service.Service')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'Booking', 'verbose_name_plural': 'Bookings'},
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='name',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='service',
            name='booking',
        ),
        migrations.AddField(
            model_name='booking',
            name='comments',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='booking',
            name='datetime',
            field=models.DateTimeField(default='2011-10-10'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='place',
            field=models.CharField(default='BOGOTA', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='price',
            field=models.DecimalField(default=90.25, max_digits=5, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='user_service',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, through='service.UserService', blank=True),
            preserve_default=True,
        ),
    ]
