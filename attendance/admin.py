from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Attendance)
admin.site.register(AttendanceRecord)
admin.site.register(AttendanceRecordImage)
admin.site.register(AttendanceRecordTest)
