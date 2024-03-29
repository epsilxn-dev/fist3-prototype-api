# Generated by Django 4.1.5 on 2023-01-23 20:17

import core.filemanager.path_saver
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('middle_name', models.CharField(blank=True, default=None, max_length=32, null=True, verbose_name='Отчество')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('is_confirmed_email', models.BooleanField(default=False, verbose_name='Почта подтверждена?')),
                ('code_email', models.TextField(blank=True, default=None, null=True, verbose_name='Токен для подтверждения')),
                ('code_email_dt', models.DateTimeField(verbose_name='Действителен до')),
                ('code_password', models.CharField(blank=True, default=None, max_length=1024, null=True, verbose_name='Токен для замены пароля')),
                ('code_password_dt', models.DateTimeField(verbose_name='Действителен до')),
                ('image', models.ImageField(blank=True, default='not-found.png', null=True, upload_to=core.filemanager.path_saver.user_image_upload_to, verbose_name='Аватар')),
                ('phone', models.CharField(blank=True, default='Не указано', max_length=15, null=True, verbose_name='Номер телефона')),
                ('is_stand', models.BooleanField(default=False)),
                ('is_graduate', models.BooleanField(default=False)),
                ('is_lecturer', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'db_table': 'usr_user',
                'ordering': ['id'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AccessTokens',
            fields=[
                ('token', models.TextField(primary_key=True, serialize=False)),
                ('valid_to', models.DateTimeField(default=None)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'usr_access_tokens',
            },
        ),
        migrations.CreateModel(
            name='RefreshTokens',
            fields=[
                ('token', models.TextField(primary_key=True, serialize=False)),
                ('valid_to', models.DateTimeField(default=None)),
                ('access', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.accesstokens')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'usr_refresh_tokens',
            },
        ),
    ]
