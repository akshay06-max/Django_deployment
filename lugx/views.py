from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')


def shop(request):
    return render(request,'shop.html')


def product_details(request):
    return render(request,'product_details.html')


def contact(request):
    return render(request,'contact.html')

def index(request):
    return render(request,'index.html')