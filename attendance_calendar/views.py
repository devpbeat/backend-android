from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class Attendance_CalendarViewSet(viewsets.ModelViewSet):
    queryset = Attendance_Calendar.objects.all()
    serializer_class = Attendance_CalendarSerializer

    def create(self, request, *args, **kwargs):
        serializer = Attendance_CalendarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = Attendance_CalendarSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def list(self, request, *args, **kwargs):
        queryset = Attendance_Calendar.objects.all()
        serializer = Attendance_CalendarSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = Attendance_CalendarSerializer(instance)
        return Response(serializer.data)
    
    