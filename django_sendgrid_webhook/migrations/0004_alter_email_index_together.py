# Generated by Django 3.2.11 on 2022-01-26 07:53

from django.db import migrations
from django.db.models import Index


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('sendgrid', '0003_auto_20190722_1007'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='email',
            index=Index(fields=['content_type', 'object_id']),
        ),
    ]
