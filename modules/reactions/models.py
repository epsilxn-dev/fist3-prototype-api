from django.db import models
from django.contrib.auth import get_user_model

from modules.document.models import Document

User = get_user_model()


class Like(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    documents = models.ManyToManyField(Document, related_name="likes", db_table="doc_document_likes")

    def __str__(self):
        return f"{self.user}"

    class Meta:
        db_table = "cmn_like"


class Dislike(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    documents = models.ManyToManyField(Document, related_name="dislikes", db_table="doc_document_dislikes")

    def __str__(self):
        return f"{self.user}"

    class Meta:
        db_table = "cmn_dislike"
