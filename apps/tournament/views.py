from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'GnexxApp | Torneos' 
    }
    
    return render(request, 'tournament/index.html', context)