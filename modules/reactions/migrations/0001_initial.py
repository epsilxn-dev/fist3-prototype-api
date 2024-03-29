# Generated by Django 4.1.5 on 2023-01-23 20:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('document', '0002_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('documents', models.ManyToManyField(to='document.document')),
            ],
            options={
                'db_table': 'cmn_like',
            },
        ),
        migrations.CreateModel(
            name='Dislike',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('documents', models.ManyToManyField(to='document.document')),
            ],
            options={
                'db_table': 'cmn_dislike',
            },
        ),
    ]
