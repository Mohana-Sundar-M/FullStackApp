from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from student import views
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    url(r'^student$',views.studentApi),
    url(r'^student$',views.studentApi),
    url(r'^student/([0-9]+)$',views.studentApi),
    path('admin/', admin.site.urls),
    
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]