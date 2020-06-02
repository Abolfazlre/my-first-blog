"""mysite URL Configuration

[...]
"""
from django.contrib import path, include
from django.urls import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]