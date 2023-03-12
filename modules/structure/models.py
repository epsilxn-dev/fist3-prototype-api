from django.db import models
from modules.document.models import Document


class Department(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    text = models.TextField()
    doc = models.ForeignKey(Document, on_delete=models.CASCADE, related_name="departments")

    class Meta:
        db_table = "fc_department"


class Direction(models.Model):
    name = models.CharField(max_length=250)
    text = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doc = models.ForeignKey(Document, on_delete=models.CASCADE, related_name="directions")

    class Meta:
        db_table = "fc_direction"


class Lecturer(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    middle_name = models.CharField(max_length=70)
    text = models.TextField()
    direction = models.ManyToManyField(Direction, db_table="fc_lecturer_direction")
    doc = models.ForeignKey(Document, on_delete=models.CASCADE, related_name="lecturers")

    class Meta:
        db_table = "fc_lecturer"
