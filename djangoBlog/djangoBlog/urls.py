from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.handle_About_Page),
    path('', views.handle_Home_Page),
]
