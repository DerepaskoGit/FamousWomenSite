from django.urls import path, register_converter
from . import views, converters
    
register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('', views.index, name='home'),
    path('main/', views.main_page, name='main'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='addpage'),
    path('feadback/', views.feadback, name='feadback'),
    path('login/', views.login, name='login'),
    path('main/post/<int:post_id>/', views.post, name='post'),
]

