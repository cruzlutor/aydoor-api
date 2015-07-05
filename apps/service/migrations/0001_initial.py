# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Advert',
                'verbose_name_plural': 'Advertices',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('datetime', models.DateTimeField()),
                ('place', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=150)),
                ('comments', models.TextField(null=True, blank=True)),
                ('advert', models.ForeignKey(related_name='advert_booking', to='service.Advert')),
                ('user_client', models.ForeignKey(related_name='client_advert', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Bookings',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='advert',
            name='booking',
            field=models.ManyToManyField(related_name='booking', through='service.Booking', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='advert',
            name='service',
            field=models.ForeignKey(to='service.Service'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='advert',
            name='user_provider',
            field=models.ForeignKey(related_name='provider_advert', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
