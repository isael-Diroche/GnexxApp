from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'GnexxApp | Equipos' 
    }
    
    return render(request, 'teams/index.html', context)