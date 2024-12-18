# Generated by Django 5.1.4 on 2024-12-17 19:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('document', '0001_initial'),
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('doc_type', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=256)),
                ('is_accept_for_comments', models.BooleanField(default=True)),
                ('is_accept_for_reactions', models.BooleanField(default=True)),
                ('is_accept_for_tags', models.BooleanField(default=True)),
                ('is_admin_level_only', models.BooleanField(default=False)),
                ('is_accept_for_files', models.BooleanField(default=False)),
                ('is_need_approve', models.BooleanField(default=True)),
                ('is_active_type', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'document"."document_type',
            },
        ),
        migrations.AddField(
            model_name='childcommentary',
            name='create_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commentary',
            name='create_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='childcommentary',
            name='parent_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.commentary'),
        ),
        migrations.AddField(
            model_name='document',
            name='create_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='document',
            name='update_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updater', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commentary',
            name='doc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.document'),
        ),
        migrations.CreateModel(
            name='DocumentDislikes',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('documents', models.ManyToManyField(related_name='dislikes', to='document.document')),
            ],
            options={
                'db_table': 'document"."dislikes',
            },
        ),
        migrations.CreateModel(
            name='DocumentLikes',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('documents', models.ManyToManyField(related_name='likes', to='document.document')),
            ],
            options={
                'db_table': 'document"."likes',
            },
        ),
        migrations.CreateModel(
            name='DocumentTags',
            fields=[
                ('name', models.CharField(max_length=32, primary_key=True, serialize=False, unique=True)),
                ('documents', models.ManyToManyField(related_name='tags', to='document.document')),
            ],
            options={
                'db_table': 'document"."tags',
            },
        ),
        migrations.AddField(
            model_name='document',
            name='doc_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.documenttype'),
        ),
    ]