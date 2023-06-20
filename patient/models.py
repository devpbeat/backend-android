from django.db import models
from base.models import TimeStampModel, Person

# Create your models here.
class Patient(TimeStampModel, Person):
    city = models.CharField(max_length=50, null=True, blank=True)
    department = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
    
    def __str__(self):
        return self.first_name
    
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
    
