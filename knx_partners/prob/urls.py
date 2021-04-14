from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('input/<int:id>', views.input, name='input'),
    path('form/', views.DeviceFormView.as_view(), name='form')
]
