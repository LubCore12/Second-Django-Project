from django.urls import path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('archive/<year4:year>', views.categories_by_year, name='archive'),
    path('cats/<int:cat_id>', views.categories_by_id, name='cats_id'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),
]