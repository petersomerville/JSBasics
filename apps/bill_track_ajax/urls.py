from django.urls import path
from . import views

app_name = 'bill_track_ajax'

urlpatterns = [
    path('', views.index, name = 'index'),
]