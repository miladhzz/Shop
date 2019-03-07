from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views import View
from .models import Product
from django.views.generic.base import ContextMixin
from django.views.decorators.http import require_POST
from .forms import CartAddProductForm, CartAddProductFormSingle
from .cart import Cart


class Product_Mixin(ContextMixin):
    def get_context_data(self, *args, **kwargs):
        ctx = super(Product_Mixin, self).get_context_data(**kwargs)
        ctx['latest_product'] = Product.objects.all()[:6]
        ctx['recently_view'] = Product.objects.all()[3:9]
        ctx['top_sel'] = Product.objects.all()[9:12]
        ctx['cart_product_from'] = CartAddProductForm()
        ctx['cart_product_from_single'] = CartAddProductFormSingle()
        return ctx


class Product_list(ListView):
    model = Product
    template_name = 'product_list.html'


class Product_detail(Product_Mixin, DetailView):
    model = Product
    template_name = 'product_detail.html'


class Home(Product_Mixin, ListView):
    model = Product
    template_name = "home.html"


class Checkout(View):

    def get(self, request):
        return render(request, 'checkout.html')


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 count=cd['count'],
                 update_count=cd['update'])
    return redirect('cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_count_from'] = CartAddProductForm(initial={'count': item['count'],
                                                                'update': True})
    return render(request, 'cart.html', {'cart': cart})
