from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.

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


data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': '''<b>Анджели́на Джоли́</b> (англ. Angelina Jolie), до 2002 года Анджелина Джоли Войт 
     (англ. Voight); род. 4 июня 1975, Лос-Анджелес) — американская актриса, кинорежиссёр, сценарист, продюсер и общественный деятель. 
     Обладательница множества престижных наград, включая «Оскар», премию «Тони» и три «Золотых глобуса». Джоли неоднократно признавалась
      самой высокооплачиваемой актрисой Голливуда.''', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулии Робертс', 'is_published': True},
]

cat_db = [
     {'url': 'category', 'name': 'Категории:'},
     {'url': '#', 'name': 'Актрисы'},
     {'url': '#', 'name': 'Певицы'},
     {'url': '#', 'name': 'Спортсменки'},
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

def post(request, post_id):
     return HttpResponse(f'<h2>Пост с id: {post_id}</h2>')

def posts(request):
     data = {
          'title':'Посты',
          'text':'Посты',
          'menu': menu,
          'posts': data_db
     }
     return render(request, 'women/posts.html', context=data)

def category(request):
     return render(request, 'women/category.html')