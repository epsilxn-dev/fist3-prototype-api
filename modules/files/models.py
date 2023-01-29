from django.db import models
from django.contrib.auth import get_user_model

from modules.document.models import Document

User = get_user_model()


class FileType(models.Model):
    file_type = models.CharField(primary_key=True, unique=True, max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.file_type

    class Meta:
        db_table = "fl_file_type"


class File(models.Model):
    file = models.FileField()
    filename = models.CharField(max_length=255)
    file_type = models.ForeignKey(FileType, on_delete=models.CASCADE)
    doc = models.ForeignKey(Document, on_delete=models.CASCADE, null=True, blank=True)
    create_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    create_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} {self.filename} {self.file_type.file_type}"

    class Meta:
        db_table = "fl_file"
        ordering = ["id"]


class UserFile(models.Model):
    file = models.FileField()
    filename = models.CharField(max_length=255)
    file_type = models.ForeignKey(FileType, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    create_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} {self.filename} {self.file_type.file_type}"

    class Meta:
        db_table = "fl_user_file"
        ordering = ["id"]
