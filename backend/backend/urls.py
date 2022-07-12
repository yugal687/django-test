"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from typing import get_args
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo import views as todo_views
# from todo.views import todo_list
from item.views import ItemView, CategoryView, ItemCategoryView
from user.views import UserView
from register.views import RegisterView
from cart.views import CartView
# from django.conf.urls import url

from register import views as register_views
# from register import RegisterAPI


# jwt
from rest_framework_jwt.views import obtain_jwt_token

from django.conf.urls.static import static
from django.conf import settings

from item import views as item_views


router = routers.DefaultRouter()
# router.register(r'todos', todo_views, 'todo')
router.register(r'items', ItemView, 'item')
router.register(r'carts', CartView, 'cart')
router.register(r'item-categories', ItemCategoryView, 'item-category')
router.register(r'categories', CategoryView, 'category')
router.register(r'users', UserView, 'user')
router.register(r'register', RegisterView, 'register')
# router.register(r'token-auth', obtain_jwt_token, basename='token-auth')



# router = routers.DefaultRouter()

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    
    # register
    path('register/', register_views.register, name='register'),

    # apis
    path('api/', include(router.urls)),


    # token jwt
    path('token-auth/', obtain_jwt_token),


    # item
    # path('item/', include('item.urls')),

    # todo
    path('todo/', todo_views.todo_list, name='todo'),

    path('', item_views.home),
    
    # users
    # path('user/', include('user.urls')),

    path('', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
