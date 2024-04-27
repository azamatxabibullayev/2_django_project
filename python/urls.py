from django.urls import path
from python.views import get_info

urlpatterns = [
    path('main', get_info)
]