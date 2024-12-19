from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.

def index(request):
    return HttpResponse('Страница приложения women')

def categories(request, cat_id):
    return HttpResponse(f'<h1>Страница категорий Women</h1><h2>id: {cat_id}</h2>')

def categories_slug(request, cat_id):   
        print(request.GET)
        return HttpResponse(f'<h1>Страница категорий Women</h1><h2>slug: {cat_id}</h2>')

def archive(request, year):
     if year > 2024:
        uri = reverse('cats_slug', args=('music', ))
        return redirect(uri)
     return HttpResponse(f'<h1>Архив </h1><h2>{year}</h2>')


def page_404(request, exception):
     return HttpResponseNotFound(f'<h1>404</h1>')

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]

def main_page(request):
     data = {
          'title': 'Главная страница',  
          'menu':menu,
          'posts': data_db
          }
     return render(request, 'women/main page.html', context=data)

def about(request):
     data = {
          'title':'О сайте',
          'text':'О сайте'
     }
     return render(request, 'women/main page.html', context=data)

