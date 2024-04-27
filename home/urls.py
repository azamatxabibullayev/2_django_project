from django.urls import path
from home.views import get_item

urlpatterns = [
    path('hello', get_item)
]