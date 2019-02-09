from django.urls import path

from shop import views

urlpatterns = [
    path('product/', views.Product.as_view(), name='product'),
    path('', views.Home.as_view(), name='home')
    ]
