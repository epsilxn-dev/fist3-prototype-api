from django.db import models
from modules.document.models import Document


class Tag(models.Model):
    name = models.CharField(primary_key=True, max_length=64, unique=True)
    documents = models.ManyToManyField(Document, related_name="tags", db_table="doc_document_tag")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "cmn_tag"
