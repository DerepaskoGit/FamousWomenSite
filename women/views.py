from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.

def index(request):
    return HttpResponse('Страница приложения women')


def page_404(request, exception):
     return HttpResponseNotFound(f'<h1>404</h1>')

menu = [
     {'title':'О сайте', 'url':'about'}, 
     {'title':'Добавить статью', 'url':'addpage'}, 
     {'title':'Обратная связь', 'url':'feedback'},
     {'title':'Войти', 'url':'login'}
     ]

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
     return render(request, 'women/about.html', context=data)

def addpage(request):
     return HttpResponse('<p> addpage </p>')

def feadback(request):
     return HttpResponse('<p> feadback </p>')

def login(request):
     return HttpResponse('<p> login </p>')

def post(request, post_id):
     return HttpResponse(f'<h2>Пост с id: {post_id}</h2>')