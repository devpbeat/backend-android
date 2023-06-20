from rest_framework import serializers
from .models import Attendance
from utils.serializers import ChoiceField


class AttendanceSerializer(serializers.ModelSerializer):
    status = ChoiceField(choices=Attendance.ATTENDANCE_STATUS)
    class Meta:
        model = Attendance
        fields = ('date', 'time', 'status')

    def create(self, validated_data):

        attendance = Attendance.objects.create(**validated_data)
        return attendance