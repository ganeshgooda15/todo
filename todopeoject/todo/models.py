from django.db import models

# Create your models here.

class Task(models.Model):
    heading = models.CharField(max_length=200)
    details = models.CharField(max_length=200)
    date = models.DateField()
    is_deleted = models.CharField(max_length=2, default = 'n')
