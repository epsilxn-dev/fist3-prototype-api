from statistics import mode
from django.contrib.auth.models import AbstractUser
from django.db import models

from core.filemanager.path_saver import user_image_upload_to


class Role(models.Model):
    name = models.CharField(primary_key=True, unique=True, max_length=32)
    int_level = models.IntegerField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "prs_role"
        ordering = ["int_level"]


class User(AbstractUser):
    middle_name = models.CharField(max_length=32, verbose_name="Отчество", default=None, blank=True, null=True)
    email = models.EmailField(verbose_name="Почта", unique=True)
    is_confirmed_email = models.BooleanField(default=False, verbose_name="Почта подтверждена?")
    code_email = models.TextField(verbose_name="Токен для подтверждения", null=True, blank=True, default=None)
    code_email_dt = models.DateTimeField(verbose_name="Действителен до", null=True, blank=True)
    code_password = models.CharField(max_length=1024, verbose_name="Токен для замены пароля",
                                     null=True, blank=True, default=None)
    code_password_dt = models.DateTimeField(verbose_name="Действителен до", null=True, blank=True)
    image = models.ImageField(upload_to=user_image_upload_to, verbose_name="Аватар", blank=True, null=True,
                              default="not-found.png")
    phone = models.CharField(max_length=15, verbose_name="Номер телефона", blank=True, null=True, default="Не указано")
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, default=None)
    is_stand = models.BooleanField(default=False)
    is_graduate = models.BooleanField(default=False)
    is_lecturer = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["password", "email"]
    USERNAME_FIELD = "username"

    class Meta:
        ordering = ["id"]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        db_table = "prs_person"

    def save(self, *args, **kwargs):
        if self.pk is None:
            avatar = self.image
            self.avatar = None
            super().save(*args, **kwargs)
            self.avatar = avatar
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class AccessTokens(models.Model):
    token = models.TextField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    valid_to = models.DateTimeField(default=None)

    class Meta:
        db_table = "prs_access_token"


class RefreshTokens(models.Model):
    token = models.TextField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    valid_to = models.DateTimeField(default=None)
    access = models.OneToOneField(AccessTokens, on_delete=models.CASCADE)

    class Meta:
        db_table = "prs_refresh_token"
