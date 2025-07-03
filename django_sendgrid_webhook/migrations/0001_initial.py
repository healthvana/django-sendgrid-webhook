# Generated manually for Django 5.2 compatibility

from django.db import migrations, models
import django.db.models.deletion
import uuid


def _new_uuid():
    """Initialisation function for reference UUID."""
    return str(uuid.uuid4())


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('email', models.CharField(max_length=512, verbose_name='addressee')),
                ('event', models.CharField(max_length=32, verbose_name='event type')),
                ('reason', models.CharField(default='', max_length=1024, verbose_name='reason')),
                ('timestamp', models.DateTimeField(verbose_name='timestamp')),
                ('uuid', models.CharField(db_index=True, default=_new_uuid, max_length=64, verbose_name='reference UUID')),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('object_id', models.PositiveIntegerField(null=True)),
            ],
            options={
                'indexes': [
                    models.Index(fields=['content_type', 'object_id'], name='sendgrid_ema_content_8b5c8c_idx'),
                ],
            },
        ),
    ]
