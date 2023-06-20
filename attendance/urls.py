from django.urls import path
from .views import AttendanceViewSet


urlpatterns = [
    path('attendance/', AttendanceViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('attendance/<str:pk>/', AttendanceViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]
