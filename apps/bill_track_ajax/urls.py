from django.urls import path
from . import views

app_name = 'bill_track_ajax'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('create_bill', views.create_bill, name='create_bill'),
    path('update_bill', views.update_bill, name='update_bill'),
    path('delete_bill', views.delete_bill, name='delete_bill'),
]