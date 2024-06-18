
# app1/models.py

from django.db import models

class Drug(models.Model):
    name = models.CharField(max_length=255)
    uses = models.TextField()

    def __str__(self):
        return self.name
