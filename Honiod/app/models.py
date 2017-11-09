"""
Definition of models.
"""

from django.db import models

class Project(models.Model):
    name = models.CharField(max_length = 512)
    added_at = models.DateTimeField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()