# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_sendgrid_webhook.models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(
                    auto_now=True, verbose_name='updated')),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('email', models.CharField(max_length=512, verbose_name='addressee')),
                ('event', models.CharField(max_length=32, verbose_name='event type')),
                ('timestamp', models.DateTimeField(verbose_name='timestamp')),
                ('uuid', models.CharField(default=django_sendgrid_webhook.models._new_uuid, max_length=64,
                                          verbose_name='reference UUID', db_index=True)),
                ('content_type', models.ForeignKey(
                    to='contenttypes.ContentType', null=True, on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddIndex(
            model_name='email',
            index=models.Index(fields=[('content_type', 'object_id')], name='django_sendgrid_webhook_email_content_type_object_id')
        ),
    ]
