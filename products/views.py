import json

from django.shortcuts import render
from django.http      import JsonResponse
from django.views     import View
from products.models  import *

class MainView(View):
    def get(self, request):
        return render(request, 'store.html')
    
class ProductView(View):
    def post(self, request):
        search = request.POST['search'] 
        products = Product.objects.filter(name__icontains=search).order_by('price')
        results = [
            {
                'store_name' : Store.objects.get(id=product.store_id).name,
                'name' : product.name,
                'plus' : product.plus,
                'price' : format(int(product.price),','),
                'img' : product.img
            } for product in products
        ]
        return render(request, 'store.html', {'results': results}, status = 200)