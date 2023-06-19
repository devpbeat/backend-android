from .models import Attendance, AttendanceRecord, AttendanceRecordImage, AttendanceRecordTest
from rest_framework import serializers

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

    
class AttendanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRecord
        fields = '__all__'

    def create(self, validated_data):
        attendance_record = AttendanceRecord.objects.create(**validated_data)
        return attendance_record


class AttendanceRecordImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRecordImage
        fields = '__all__'
    

class AttendanceRecordTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRecordTest
        fields = '__all__'

