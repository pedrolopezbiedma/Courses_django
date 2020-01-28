from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.handle_SignUp_Page, name='signup'),
    path('login/', views.handle_Login_Page, name='login'),
    path('logout/', views.handle_Logout_Page, name='logout')
]
