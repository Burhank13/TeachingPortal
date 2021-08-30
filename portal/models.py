from django.db import models
from datetime import datetime
from django import forms

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=100)
    profession = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = "people"
    
    def __str__(self):
        return self.name + " (" + self.profession + ")"


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