from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'GnexxApp | Configuración'
    }
    
    return render(request, 'settings/index.html', context)