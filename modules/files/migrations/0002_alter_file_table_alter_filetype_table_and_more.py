# Generated by Django 4.1.5 on 2023-02-21 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='file',
            table='fsDocumentFile',
        ),
        migrations.AlterModelTable(
            name='filetype',
            table='fsFileType',
        ),
        migrations.AlterModelTable(
            name='userfile',
            table='fsPersonFile',
        ),
    ]
