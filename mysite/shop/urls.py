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
    path('cart/update/<int:product_id>', views.cart_update, name='cart_update'),
    path('cart/remove/<int:product_id>', views.cart_remove, name='cart_remove'),
    path('checkout/', views.checkout, name='checkout'),
    path('to_bank/<int:order_id>', views.to_bank, name='to_bank'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
