from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.handle_Home_Page),
    path('about/', views.handle_About_Page),
    path('articles/', include('articles.urls'))
]

urlpatterns += staticfiles_urlpatterns()
