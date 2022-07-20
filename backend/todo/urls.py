from django.urls import path, include
from . import views


#users
urlpatterns = [
    path('api/todos/', views.todo_list, name='todo'),
    path('api/todos/<int:pk>/',views.todo_detail, name='todo-detail'),
]




