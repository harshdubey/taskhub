from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def Our_packages(request):
    return render(request, 'our_pkg.html')

def contact(request):
    return render(request, 'contact.html')