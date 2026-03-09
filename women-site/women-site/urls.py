from xml.etree.ElementInclude import include

from women.views import page_not_found
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls')),
]

handler404 = page_not_found