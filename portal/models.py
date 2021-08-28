from django.db import models
from datetime import datetime

# Create your models here.
class Test(models.Model):
    test_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    link = models.URLField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    marks_available = models.PositiveIntegerField(default=20)

    def __str__(self):
        return self.test_name

class Assignment(models.Model):
    assignment_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    link = models.URLField()
    upload_time = models.DateTimeField(default=datetime.now)
    deadline = models.DateTimeField()
    marks_available = models.PositiveIntegerField(default=20)

    def __str__(self):
        return self.assignment_name