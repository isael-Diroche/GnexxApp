from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'GnexxApp | Comunidad' 
    }
    
    return render(request, 'community/index.html', context)