# Generated by Django 3.2.14 on 2022-11-25 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0006_alter_cycle_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueLabelGroup',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issuelabelgroup_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group', to='db.label')),
            ],
            options={
                'verbose_name': 'Issue Label Group',
                'verbose_name_plural': 'Issue Label Groups',
                'db_table': 'issue_label_group',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='LabelGroup',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='labelgroup_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('labels', models.ManyToManyField(blank=True, related_name='label_groups', through='db.IssueLabelGroup', to='db.Label')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_labelgroup', to='db.project')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='labelgroup_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Last Modified By')),
                ('workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workspace_labelgroup', to='db.workspace')),
            ],
            options={
                'verbose_name': 'Label Group',
                'verbose_name_plural': 'Label Groups',
                'db_table': 'label_group',
                'ordering': ('-created_at',),
                'unique_together': {('name', 'project')},
            },
        ),
        migrations.AddField(
            model_name='issuelabelgroup',
            name='label_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='label_group', to='db.labelgroup'),
        ),
        migrations.AddField(
            model_name='issuelabelgroup',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_issuelabelgroup', to='db.project'),
        ),
        migrations.AddField(
            model_name='issuelabelgroup',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issuelabelgroup_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Last Modified By'),
        ),
        migrations.AddField(
            model_name='issuelabelgroup',
            name='workspace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workspace_issuelabelgroup', to='db.workspace'),
        ),
    ]
