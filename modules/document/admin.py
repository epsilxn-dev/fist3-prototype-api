from django.contrib import admin
from .models import Document, DocumentType


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("id", "doc_type", "is_ready_for_publish")
    ordering = ("is_ready_for_publish", "-id")


@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ("doc_type", )
