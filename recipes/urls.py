from django.urls import path
from recipes.views import *

urlpatterns = [
    path('', my_home),
]