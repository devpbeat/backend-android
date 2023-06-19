from django.urls import path
from .views import PatientViewSet


urlpatterns = [
    path('patient/', PatientViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('patient/<str:pk>/', PatientViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]
