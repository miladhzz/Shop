from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from .models import Product
from django.views.generic.base import ContextMixin


class Product_Mixin(ContextMixin):
    def get_context_data(self, *args, **kwargs):
        ctx = super(Product_Mixin, self).get_context_data(**kwargs)
        ctx['latest_product'] = Product.objects.all()[:5]
        return ctx


class Product_list(ListView):
    model = Product
    template_name = 'product_list.html'


class Product_detail(Product_Mixin, DetailView):
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
