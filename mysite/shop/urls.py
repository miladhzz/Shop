from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from shop import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('shop/', views.Product_list.as_view(), name='product'),
    path('shop/<slug:slug>/', views.Product_detail.as_view(), name='product-detail'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>', views.cart_add, name='cart_add'),
    path('checkout/', views.Checkout.as_view(), name='checkout'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
