from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views import View
from .models import Product, OrderItem
from django.views.generic.base import ContextMixin
from django.views.decorators.http import require_POST
from .forms import CartAddProductForm, CartUpdateProductForm, OrderCheckoutForm
from .cart import Cart


class Form_Mixin(ContextMixin):
    def get_context_data(self, *args, **kwargs):
        ctx = super(Form_Mixin, self).get_context_data(**kwargs)
        ctx['cart_product_from'] = CartAddProductForm()
        return ctx


class TopSel_Mixin(ContextMixin):
    def get_context_data(self, *args, **kwargs):
        ctx = super(TopSel_Mixin, self).get_context_data(**kwargs)
        ctx['top_sel'] = Product.objects.all()[9:12]
        return ctx


class Recently_Mixin(ContextMixin):
    def get_context_data(self, *args, **kwargs):
        ctx = super(Recently_Mixin, self).get_context_data(**kwargs)
        ctx['recently_view'] = Product.objects.all()[3:9]
        return ctx


class Latest_Mixin(ContextMixin):
    def get_context_data(self, *args, **kwargs):
        ctx = super(Latest_Mixin, self).get_context_data(**kwargs)
        ctx['latest_product'] = Product.objects.all()[3:9]
        return ctx


class Product_list(Form_Mixin, ListView):
    model = Product
    template_name = 'product_list.html'


class Product_detail(TopSel_Mixin, Latest_Mixin, Form_Mixin, DetailView):
    model = Product
    template_name = 'product_detail.html'


class Home(TopSel_Mixin, Recently_Mixin, Latest_Mixin, Form_Mixin, ListView):
    model = Product
    template_name = "home.html"


def checkout(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCheckoutForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         count=item['count'])
            # Clear the cart
            cart.clear()
            return redirect('to_bank', order_id=order.random_order_id)

    else:
        form = OrderCheckoutForm()
    return render(request, 'checkout.html', {'cart': cart,
                                             'form': form})


def to_bank(request, order_id):
    return render(request, 'bank.html', {'order_id': order_id})


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


@require_POST
def cart_update(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartUpdateProductForm(request.POST)
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
        item['update_count_from'] = CartUpdateProductForm(initial={'count': item['count'],
                                                                      'update': True})
    return render(request, 'cart.html', {'cart': cart})
