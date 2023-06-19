from django.urls import path, include
from .views import *

urlpatterns = [
    path('attendance_calendar/', Attendance_CalendarViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('attendance_calendar/<str:pk>/', Attendance_CalendarViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]



