# api/urls.py
from django.urls import path, include
from rest_framework import routers
from api import views

# Crea un enrutador y registra el viewset
router = routers.DefaultRouter()
router.register(r'programmers', views.ProgrammerViewSet)

# Incluye el enrutador en tus URLs
urlpatterns = [
    path('api/v1/', include(router.urls)),  # Cambia esto para incluir la ruta base
]
