from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('upload/',upload,name="upload"),
    path('design/',design,name="design"),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
