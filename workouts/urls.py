from django.urls import path
from . import views

urlpatterns = [
  path('', views.workouts, name='workouts'),
  path('debt.html', views.debt, name='debt'),
]