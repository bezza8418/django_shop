from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.home, name='home'),           # Главная страница
    path('contacts/', views.contacts, name='contacts'),  # Страница контактов
]
