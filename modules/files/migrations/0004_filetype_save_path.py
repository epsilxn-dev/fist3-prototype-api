# Generated by Django 4.1.7 on 2023-03-11 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_alter_file_table_alter_filetype_table_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='filetype',
            name='save_path',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
