import json, requests

from django.http import JsonResponse
from django.shortcuts import render
from apps.bill_track_ajax.models import User

def index(request):
    return render(request, 'bill_track_ajax/index.html')

def data(request):
    if request.method == 'POST':
        try:
            return JsonResponse(requests.get(request.POST['url']).text, safe=False)
        except:
            return JsonResponse({'error': 'Request failed'})

    return JsonResponse({'error': 'GET request not allowed'})

def create_bill(request):
    if request.method == 'POST':
        print(request.POST)
        return JsonResponse({'createbill': 'blah'})

def update_bill(request, bill_id):
    if request.method == 'POST':
        print(request.POST)
        return JsonResponse({'updatebill': 'blahblah'})

def delete_bill(request, bill_id):
    if request.method == 'POST':
        print(request.POST)
        return JsonResponse({'deletebill': 'blahblahblah'})
