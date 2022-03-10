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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo.views import TodoView
from item.views import ItemView
from user.views import UserView
from django.conf.urls import url

from item import views

# jwt
from rest_framework_jwt.views import obtain_jwt_token

from django.conf.urls.static import static
from django.conf import settings

from item import views as item_views


router = routers.DefaultRouter()
router.register(r'todos', TodoView, 'todo')
router.register(r'items', ItemView, 'item')
router.register(r'users', UserView, 'user')


# router = routers.DefaultRouter()

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # apis
    path('api/', include(router.urls)),
    # token jwt
    path('token-auth/', obtain_jwt_token),

    # item
    path('item/', include('item.urls')),

    # path('signup/', item_views.signup, name='signup'),

    # users
    path('', item_views.index),
    path('signup/', item_views.hello),


    path('user/', include('user.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
