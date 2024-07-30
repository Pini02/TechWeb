from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, template_name='home.html')

def who(request):
    return render(request, template_name='who.html')
def contacts(request):
    return render(request, template_name='contacts.html')

def prices(request):
    return render(request, template_name='prices.html')