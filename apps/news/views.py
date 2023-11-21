from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'GnexxApp | Noticias' 
    }
    
    return render(request, 'news/index.html', context)