from django.urls import path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index),
    path('archive/<year4:year>', views.categories_by_year),
    path('cats/<int:cat_id>/', views.categories_by_id),
    path('cats/<slug:cat_slug>/', views.categories_by_slug),
]