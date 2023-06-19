from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', include('attendance.urls')),
    path('', include('clinic.urls')),
    path('', include('doctors.urls')),
    path('', include('patient.urls')),
    path('', include('attendance_calendar.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('', include('.urls')),
]