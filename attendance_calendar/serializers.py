from rest_framework import serializers
from .models import Attendance_Calendar

class Attendance_CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance_Calendar
        fields = '__all__'

    def create(self, validated_data):
        attendance_calendar = Attendance_Calendar.objects.create(**validated_data)
        return attendance_calendar
    
    def update(self, instance, validated_data):
        instance.date_start = validated_data.get('date_start', instance.date_start)
        instance.date_end = validated_data.get('date_end', instance.date_end)
        instance.clinic = validated_data.get('clinic', instance.clinic)
        instance.doctors = validated_data.get('doctors', instance.doctors)
        instance.patients = validated_data.get('patients', instance.patients)
        instance.created_by = validated_data.get('created_by', instance.created_by)
        instance.updated_by = validated_data.get('updated_by', instance.updated_by)
        instance.save()
        return instance
    
    def delete(self, instance):
        instance.delete()
        return instance
    
    def list(self, queryset):
        serializer = Attendance_CalendarSerializer(queryset, many=True)
        return serializer.data
    
    def retrieve(self, instance):
        serializer = Attendance_CalendarSerializer(instance)
        return serializer.data
    
