from django.db import models
from base.models import TimeStampModel
from django.contrib.auth.models import User
from django.utils import timezone
from clinic.models import Clinic
from patient.models import Patient
from doctors.models import Doctor
# Create your models here.

class Attendance_Calendar(TimeStampModel, models.Model):
    date_start = models.DateTimeField(default=timezone.now)
    date_end = models.DateTimeField(default=(timezone.now()+timezone.timedelta(days=30)))
    clinic = models.ForeignKey(Clinic, on_delete=models.PROTECT)
    doctors = models.ManyToManyField(Doctor)
    patients = models.ManyToManyField(Patient)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="updated_by")
    time_start = models.TimeField(default=timezone.now)
    time_end = models.TimeField(default=(timezone.now()+timezone.timedelta(hours=8)))

    def __str__(self):
        return self.clinic.name + " " + str(self.date_start) + " " + str(self.date_end)
    
    def save(self, *args, **kwargs):
        super(Attendance_Calendar, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        super(Attendance_Calendar, self).delete(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Attendance Calendar"
        ordering = ['-date_start']
        db_table = 'attendance_calendar'
        managed = True
        unique_together = ('date_start', 'date_end', 'clinic')
        permissions = (
            ('doctor_view_calendar', 'Doctor view attendance calendar'),
            ('patient_view_calendar', 'Patient view attendance calendar'),
        )
    




    

    
