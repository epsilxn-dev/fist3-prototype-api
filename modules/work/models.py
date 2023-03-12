from django.db import models

from modules.document.models import Document


class Company(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=320, null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)
    doc = models.ForeignKey(Document, on_delete=models.CASCADE, related_name="companies")


class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=300)
    text_markup = models.TextField()
    fork_start = models.FloatField(null=True, blank=True)
    fork_end = models.FloatField(null=True, blank=True)
    currency_type = models.CharField(max_length=10, default="руб.")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies_set")
    doc = models.ForeignKey(Document, on_delete=models.CASCADE, related_name="vacancies")
