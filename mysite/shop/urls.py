from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from shop import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('product/', views.Product.as_view(), name='product'),
    path('cart/', views.Cart.as_view(), name='cart'),
    path('checkout/', views.Checkout.as_view(), name='checkout'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
