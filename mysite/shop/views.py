from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from .models import Product


# Create your views here
class Product_list(ListView):
    model = Product
    template_name = 'product_list.html'


class Product_detail(DetailView):
    model = Product
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
