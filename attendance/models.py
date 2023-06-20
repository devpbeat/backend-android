from django.db import models
# from doctors.models import Doctor, Speciality
from patient.models import Patient
# from hospitals.models import Hospital, Room
from base.models import TimeStampModel
# Create your models here.



class Attendance(TimeStampModel):
    ATTENDANCE_STATUS = (
    ('P', 'Pending'),
    ('A', 'Attended'),
    ('C', 'Cancelled'),
)
    room = models.CharField(null=True, blank=True)
    speciality = models.CharField(null=True, blank=True)
    doctor = models.CharField(null=True, blank=True)
    hospital = models.CharField(null=True, blank=True)
    observations = models.TextField(null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    status = models.CharField(choices=ATTENDANCE_STATUS, max_length=1, default='P')

    class Meta:
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendances'

    def __str__(self):
        return f"{self.patient.first_name} {self.patient.last_name} - {self.date} - {self.time} - {self.status} - {self.speciality} - {self.doctor} - {self.hospital}"
    
