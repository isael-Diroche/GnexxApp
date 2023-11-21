from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'GnexxApp | Login' 
    }
    
    return render(request, 'auth/index.html', context)