from django.db import models
from base.models import TimeStampModel, Person
# from auditlog.registry import auditlog
import datetime

# Create your models here.

class Doctor(TimeStampModel, Person):
    speciality = models.CharField(max_length=200)
    license = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    hospital = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='doctors', null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'
        ordering = ['first_name', 'last_name']
    
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
    
    def get_short_name(self):
        return self.first_name
    
    def get_age(self):
        years = (datetime.now().date() - self.birth_date).days / 365
        return int(years)
    
# auditlog.register(Doctor)
