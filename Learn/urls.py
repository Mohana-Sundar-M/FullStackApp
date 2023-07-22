from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from student import views

urlpatterns = [
    url(r'^student$',views.studentApi),
    url(r'^student$',views.studentApi),
    url(r'^student/([0-9]+)$',views.studentApi),
    path('admin/', admin.site.urls),
]