from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Service
from .utils import haversine


# 🌍 Nearby services API
@api_view(['GET'])
def nearby_services(request):
    user_lat = float(request.GET.get('lat'))
    user_lon = float(request.GET.get('lon'))
    max_km = float(request.GET.get('radius', 10))

    nearby = []
    for service in Service.objects.filter(is_available=True):
        distance = haversine(user_lat, user_lon, service.latitude, service.longitude)
        if distance <= max_km:
            nearby.append({
                'title': service.title,
                'category': service.category,
                'provider': service.provider.username,
                'distance_km': round(distance, 2),
                'price_per_hour': service.price_per_hour
            })
    return Response(nearby)


# 🖥️ Frontend HTML view
def frontend(request):
    return render(request, 'services/nearby.html')
