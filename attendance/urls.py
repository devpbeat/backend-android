from django.urls import path
from .views import (
    AttendanceRecordTestViewSet,
    AttendanceViewSet,
    AttendanceRecordImageViewSet,
    AttendanceRecordViewSet
)

urlpatterns = [
    path('attendance_test/', AttendanceRecordTestViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('attendance_test/<str:pk>/', AttendanceRecordTestViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('attendance/', AttendanceViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('attendance/<str:pk>/', AttendanceViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('attendance_image/', AttendanceRecordImageViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('attendance_image/<str:pk>/', AttendanceRecordImageViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('attendance_record/', AttendanceRecordViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('attendance_record/<str:pk>/', AttendanceRecordViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]
