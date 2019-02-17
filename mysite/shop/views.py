from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from shop import models


# Create your views here
class Product(View):

    def get(self, request):
        products = models.Product.objects.all()
        return render(request, 'product.html', {'products': products})


class Home(View):

    def get(self, request):
        return render(request, 'home.html')


class Cart(View):

    def get(self, request):
        return render(request, 'cart.html')


class Checkout(View):

    def get(self, request):
        return render(request, 'checkout.html')
