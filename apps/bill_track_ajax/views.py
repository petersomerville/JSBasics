import json, requests

from django.http import JsonResponse
from django.shortcuts import render, redirect
from apps.bill_track_ajax.models import BillItem
from apps.login_reg.models import User


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
        user_id = request.session['user_id']
        description = request.POST['html_description']
        amount = request.POST['html_amount']

        bill = BillItem.objects.create(
            user_id = user_id,
            description = description,
            amount = amount
        )

        return JsonResponse({
            "description": description,
            "amount": amount,
            "delete_url": redirect('bill_track_ajax:delete_bill', bill_id=bill.id).url,
            "update_url": redirect('bill_track_ajax:update_bill', bill_id=bill.id).url
        })

def delete_bill(request, bill_id):
    if request.method == 'POST':
        print(request.POST)
        bill = BillItem.objects.get(id = bill_id)
        bill.delete()
        return JsonResponse({'deletebill': 'blahblahblah'})


def update_bill(request, update_url):
    if request.method == 'POST':
        print(request.POST)
        return JsonResponse({'updatebill': 'blahblah'})



# def update_bill(request, bill_id):
#     if request.method == 'POST':
#         bill = BillItem.objects.get(id = bill_id)
#         bill.description = request.POST['html_description']
#         bill.amount = request.POST['html_amount']
#         bill.save()

#         return redirect('bill_tracker:index')
#     return render(request, 'bill_tracker/index.html')