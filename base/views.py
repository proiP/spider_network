from django.shortcuts import render

# Create your views here.

def home_view(request):
    template = 'body/home.html'
    return render(request, template)
    
