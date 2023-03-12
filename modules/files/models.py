from django.db import models
from django.contrib.auth import get_user_model

from modules.document.models import Document

User = get_user_model()


class FileType(models.Model):
    file_type = models.CharField(primary_key=True, unique=True, max_length=64)
    description = models.TextField()
    save_path = models.CharField(max_length=255, null=True, blank=True, default=None)

    def __str__(self):
        return self.file_type

    class Meta:
        db_table = "fs_file_type"


class File(models.Model):
    file = models.CharField(max_length=4000)
    filename = models.CharField(max_length=255)
    file_type = models.ForeignKey(FileType, on_delete=models.CASCADE)
    doc = models.ForeignKey(Document, on_delete=models.CASCADE, null=True, blank=True, related_name="files")
    create_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    create_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} {self.filename} {self.file_type.file_type}"

    class Meta:
        db_table = "fs_file"
        ordering = ["id"]

