# habits/urls.py
from django.urls import path
from . import views

# Задаём пространство имён для приложения (app_name), 
# чтобы в шаблонах использовать красивые ссылки вида {% url 'habits:list' %}
app_name = 'habits'

urlpatterns = [
    # Пока оставляем пустым, сюда мы пропишем наши будущие CBV (вьюхи)
    # path('', views.HabitListView.as_view(), name='list'),
]