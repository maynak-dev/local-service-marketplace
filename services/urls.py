from django.urls import path
from .views import nearby_services, frontend

urlpatterns = [
    path('', frontend, name='home'),  # Frontend homepage
    path('nearby/', nearby_services, name='nearby-services'),  # API
]