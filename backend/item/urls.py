from django.urls import path
from . import views
from rest_framework import routers
from django.urls import include, path
#users
# from .views import current_user, UserList
 
# from . import views  

router = routers.DefaultRouter()
router.register(r'post', views.ItemView,'item'),
urlpatterns = router.urls

# urlpatterns = [
# path('index/', include(views.index)),    

# ]
#users
# urlpatterns += [
#     path('current_user/', current_user),
#     path('users/', UserList.as_view())
# ]