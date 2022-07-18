from django.urls import path, include
from . import views


#users
urlpatterns = [
    path('api/todos/', views.todo_list, name='todo'),
]




