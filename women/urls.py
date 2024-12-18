from django.urls import path, register_converter
from . import views, converters
    
register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('', views.index, name='home'),
    path('cats/<int:cat_id>/', views.categories, name='cats'),
    path('cats/<slug:cat_id>/', views.categories_slug, name='cats_slug'),
    path('archive/<yyyy:year>/', views.archive, name='archive'),
    path('main/', views.main_page),
    path('about/', views.about)
]

