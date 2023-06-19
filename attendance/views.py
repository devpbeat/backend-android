from django.shortcuts import render
from rest_framework import viewsets
from .models import AttendanceRecordTest, Attendance, AttendanceRecordImage, AttendanceRecord
from .serializers import AttendanceRecordTestSerializer, AttendanceSerializer, AttendanceRecordImageSerializer, AttendanceRecordSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.

class AttendanceRecordTestViewSet(viewsets.ModelViewSet):
    serializer_class = AttendanceRecordTestSerializer
    queryset = AttendanceRecordTest.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = AttendanceSerializer
    queryset = Attendance.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class AttendanceRecordImageViewSet(viewsets.ModelViewSet):
    serializer_class = AttendanceRecordImageSerializer
    queryset = AttendanceRecordImage.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class AttendanceRecordViewSet(viewsets.ModelViewSet):
    serializer_class = AttendanceRecordSerializer
    queryset = AttendanceRecord.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
