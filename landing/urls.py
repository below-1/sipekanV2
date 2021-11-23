from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('info', views.get_info, name='get_info')
]
