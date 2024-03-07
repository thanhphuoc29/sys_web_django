from django.shortcuts import render,redirect
from .models import CartItem
import json
from django.http import JsonResponse
# Create your views here.

def cart_items(request):
    items = CartItem.objects.all()
    return render(request, 'cart.html',{'items':items})

def remove_item(request,item_id):
    item = CartItem.objects.get(id=item_id)
    item.delete()
    return redirect('/cart')

def save_item(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        res = {}
        try:
            item = CartItem.objects.get(id=data['id'])
            item.quantity = data['quantity']
            item.status = data['status']
            item.save()
            res = {'status':'OK'}
        except:
            res= {'status':'False'}
        return JsonResponse(res)