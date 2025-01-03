from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from women.models import Data_db

def index(request):
    return HttpResponse('Страница приложения women')


def page_404(request, exception):
     return HttpResponseNotFound(f'<h1>404</h1>')

menu = [
     {'title':'About', 'url':'about'}, 
     {'title':'Add post', 'url':'addpage'}, 
     {'title':'Обратная связь', 'url':'feadback'},
     {'title':'Login', 'url':'login'},
     {'title':'fw', 'url':'main'},
     {'title':'Posts', 'url':'posts'}
     ]


cat_db = [
     {'url': 'category', 'name': 'Категории:'},
     {'url': '#', 'name': 'Актрисы'},
     {'url': '#', 'name': 'Певицы'},
     {'url': '#', 'name': 'Спортсменки'},
]

def main_page(request):
     posts = Data_db.Published_manager.all()

     data = {
          'title': 'Главная страница',  
          'menu':menu,
          'posts': posts
          }
     return render(request, 'women/main page.html', context=data)

def about(request):
     data = {
          'title':'О сайте',
          'text':'О сайте',
          'menu': menu,
     }
     return render(request, 'women/about.html', context=data)

def addpage(request):
     data = {
          'title':'Добавить статью',
          'text':'Добавить статью',
          'menu': menu,
     }
     return render(request, 'women/addpage.html', context=data)

def feadback(request):
     data = {
          'title':'Обратная связь',
          'text':'Обратная связь',
          'menu': menu,
     }
     return render(request, 'women/feadback.html', context=data)

def login(request):
     data = {
          'title':'Авторизация',
          'text':'Авторизация',
          'menu': menu,
     }
     return render(request, 'women/login.html', context=data)

def post(request, post_slug):
     post = get_object_or_404(Data_db, slug=post_slug)

     data = {
          'title':post.title,
          'menu':menu,
          'post':post,
          'cat_selected': 1,
     }

     return render(request, 'women/post.html', context=data)

def posts(request):
     posts = Data_db.objects.filter(is_published=1)

     data = {
          'title':'Посты',
          'text':'Посты',
          'menu': menu,
          'posts': posts
     }
     return render(request, 'women/posts.html', context=data)

def category(request):
     return render(request, 'women/category.html')