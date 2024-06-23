
# app1/models.py

from django.db import models

from django.db import models

class Appointment(models.Model):
    p_name = models.CharField(max_length=100)
    p_email = models.EmailField()
    p_address = models.CharField(max_length=255)
    p_date_time = models.DateTimeField()
    def __str__(self):
        return f"{self.p_name} - {self.p_date_time}"
    
class Doctor(models.Model):
    Doctor_name=models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return self.Doctor_name