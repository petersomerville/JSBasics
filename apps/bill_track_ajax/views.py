import json, requests

from django.http import JsonResponse
from django.shortcuts import render
from apps.bill_track_ajax.models import User

def index(request):
    return render(request, 'bill_track_ajax/index.html')

# Create your views here.
