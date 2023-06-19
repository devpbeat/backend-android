from django.db import models
from base.models import TimeStampModel
from doctors.models import Doctor

# Create your models here.
class Hospital(TimeStampModel, models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    ruc = models.CharField(max_length=200)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
    
class Clinic(Hospital):
    logo = models.ImageField(upload_to='clinic_logo', blank=True)

    class Meta:
        verbose_name = 'Clinic'
        verbose_name_plural = 'Clinics'
    
    def __str__(self):
        return self.name
    

class Specialization(TimeStampModel, models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = 'Specialization'
        verbose_name_plural = 'Specializations'
    
    def __str__(self):
        return self.name
    
class DoctorsInSpecialization(TimeStampModel, models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    specialization = models.ForeignKey(Specialization, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = 'Doctor in Specialization'
        verbose_name_plural = 'Doctors in Specialization'
    
    def __str__(self):
        return self.doctor.first_name + ' ' + self.doctor.last_name + ' - ' + self.specialization.name
    