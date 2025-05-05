from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('upload/',upload,name="upload"),
    path('design/',design,name="design")
]
