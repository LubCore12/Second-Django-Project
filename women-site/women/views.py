from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def categories_by_id(request, cat_id):
    return HttpResponse(f"<h1>Статьи по айди</h1><p>id: {cat_id}</p>")

def categories_by_slug(request, cat_slug):
    print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")

def categories_by_year(request, year):
    if year > 2026:
        raise Http404()

    return HttpResponse(f"<h1>Архив по годам</h1><p>year: {year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

