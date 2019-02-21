from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from django.views import View
from shop import models


# Create your views here
class Product_list(ListView):
    model = models.Product
    template_name = 'product_list.html'


class Product_detail(ListView):
    model = models.Product
    template_name = 'product_detail.html'


class Home(View):

    def get(self, request):
        return render(request, 'home.html')


class Cart(View):

    def get(self, request):
        return render(request, 'cart.html')


class Checkout(View):

    def get(self, request):
        return render(request, 'checkout.html')
