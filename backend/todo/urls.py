from django.urls import path, include
from . import views
from rest_framework import routers

#users
# from .views import current_user, UserList  

router = routers.DefaultRouter()
router.register(r'post', views.TodoView,'todo'),
urlpatterns = router.urls


#users
# urlpatterns += [
#     path('current_user/', current_user),
#     path('users/', UserList.as_view())
# ]

# test
# urlpatterns = [  
#     path('', views.todo_list),
#     path('', include(router.urls)),
# ]
