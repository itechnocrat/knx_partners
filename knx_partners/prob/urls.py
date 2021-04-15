from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('input/1', views.DevicesFormView.as_view(), name='form'),
    path('input/<int:id>', views.input, name='input'),
    # path('form/', views.DevicesFormView.as_view(), name='form'),
    path('devices/', views.DevicesListView.as_view(), name='devices')
]
