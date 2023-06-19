from django.db import models
from doctors.models import Doctor
from patient.models import Patient
from clinic.models import Clinic
from base.models import TimeStampModel

# Create your models here.

class Attendance(TimeStampModel, models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    clinic = models.ForeignKey(Clinic, on_delete=models.PROTECT)
    date = models.DateField()
    time = models.TimeField()
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendances'

    def __str__(self):
        return self.patient.name + ' ' + self.patient.last_name + ' - ' + self.doctor.name + ' ' + self.doctor.last_name
    
class AttendanceRecord(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.PROTECT)
    symptoms = models.TextField()
    diagnosis = models.TextField()
    prescription = models.TextField()
    # Add other relevant fields like test results, etc.

    def __str__(self):
        return f"Medical Record of {self.patient.name}"
    

class AttendanceRecordImage(models.Model):
    attendance_record = models.ForeignKey(AttendanceRecord, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='attendance_record_image', blank=True)

    def __str__(self):
        return f"Image of {self.attendance_record.patient.name}"

class AttendanceRecordTest(models.Model):
    attendance_record = models.ForeignKey(AttendanceRecord, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=200)
    test_result = models.CharField(max_length=200)

    def __str__(self):
        return f"Test of {self.attendance_record.patient.name}"
    
