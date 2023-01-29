from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class DocumentType(models.Model):
    doc_type = models.CharField(primary_key=True, unique=True, max_length=64)
    description = models.CharField(max_length=256)
    is_accept_for_comments = models.BooleanField(default=True)
    is_accept_for_reactions = models.BooleanField(default=True)
    is_accept_for_tags = models.BooleanField(default=True)
    is_admin_level_only = models.BooleanField(default=False)

    class Meta:
        db_table = "doc_document_type"


class Document(models.Model):
    doc_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    json_data = models.JSONField(null=True)
    is_moderated = models.BooleanField(default=True)
    is_ready_for_publish = models.BooleanField(default=True)

    create_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True)

    class Meta:
        db_table = "doc_document"
        ordering = ["id"]

