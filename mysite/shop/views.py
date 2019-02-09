from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here
class Product(View):

    def get(self, request):
        return HttpResponse("Product")


class Home(View):

    def get(self, request):
        return HttpResponse("Home Page")
