from django.contrib.auth import get_user_model
from django.db import models

from modules.document.models import Document

User = get_user_model()


class Commentary(models.Model):
    text = models.TextField()
    doc = models.ForeignKey(Document, on_delete=models.CASCADE)
    create_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        db_table = "cmn_commentary"
        ordering = ["id"]


class ChildCommentary(models.Model):
    text = models.TextField()
    parent_comment = models.ForeignKey(Commentary, on_delete=models.CASCADE)
    create_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        db_table = "cmn_child_commentary"
        ordering = ["id"]

