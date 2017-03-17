from django.shortcuts import render
import nmap

# Create your views here.

def home_view(request):
    template = 'body/home.html'
    nm = nmap.PortScanner()
    print nm
    return render(request, template)
    
