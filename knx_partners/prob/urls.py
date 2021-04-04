from django.urls import path
from .views import get_name

urlpatterns = [
    path('handler-form/', get_name),
    path('', get_name),
]
