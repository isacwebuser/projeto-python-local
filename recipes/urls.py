from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.my_home, name="home"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]
