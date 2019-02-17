from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')

def charts(request):
    return render(request, 'charts.html')

def elements(request):
    return render(request, 'elements.html')

def login(request):
    return render(request, 'login.html')

def panels(request):
    return render(request, 'panels.html')

def widgets(request):
    return render(request, 'widgets.html')