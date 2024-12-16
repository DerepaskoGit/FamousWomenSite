from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('Страница приложения women')

def categories(request, cat_id):
    return HttpResponse(f'<h1>Страница категорий Women</h1><p>id: {cat_id}</p>')

def categories_slug(request, cat_id):
        return HttpResponse(f'<h1>Страница категорий Women</h1><p>slug: {cat_id}</p>')

def archive(request, year):
     return HttpResponse(f'<h1>Архив </h1><h2>{year}</h2>')

