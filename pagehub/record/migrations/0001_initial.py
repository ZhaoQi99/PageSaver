# Generated by Django 5.0.7 on 2024-08-02 07:19

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snapshot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('url', models.URLField(db_index=True)),
                ('title', models.CharField(blank=True, db_index=True, default='', max_length=512)),
            ],
            options={
                'verbose_name': '快照',
                'verbose_name_plural': '快照',
                'db_table': 'snapshot',
            },
        ),
        migrations.CreateModel(
            name='SnapshotResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('format', models.CharField(choices=[('PDF', 'PDF'), ('MHTML', 'MHTML文件')], max_length=10)),
                ('path', models.FileField(upload_to='')),
                ('snapshot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='record.snapshot',related_name='results')),
            ],
            options={
                'verbose_name': '快照结果',
                'verbose_name_plural': '快照结果',
                'db_table': 'snapshot_result',
                'unique_together': {('snapshot', 'format')},
            },
        ),
    ]
