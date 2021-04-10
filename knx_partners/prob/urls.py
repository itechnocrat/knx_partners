from django.urls import path
from . import views

urlpatterns = [
    # path('handler-form/', views.get_name),
    # path('', get_name),
    path('', views.index, name='index'),
    path('input/<int:id>', views.input, name='input'),
    path('output/<int:id>', views.output, name='output'),
    path('device/<int:id>', views.device, name='device'),
    path('sensor/<int:id>', views.sensor, name='sensor'),
    path('devicewa/<int:id>', views.devicewa, name='device_with_automation'),
    path('socket/<int:id>', views.socket, name='socket'),
    path('light/<int:id>', views.light, name='light'),
]
