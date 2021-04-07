from django.urls import path
from . import views

urlpatterns = [
    path('handler-form/', views.get_name),
    # path('', get_name),
    path('', views.index, name='index'),
]
