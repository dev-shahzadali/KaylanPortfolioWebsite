from .models import Category
from django.urls import resolve

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)

def current_path(request):
    return{
        'current_path': resolve(request.path_info).url_name
    }

