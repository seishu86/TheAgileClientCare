from django.shortcuts import render

def home(request):
    return render(request,'app/home.html')

def order(request):
    return render(request,'app/order.html')
