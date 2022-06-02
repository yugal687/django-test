from django.urls import path
from . import views
from rest_framework import routers
from django.urls import path
#users
# from .views import current_user, UserList
 
# from . import views  

router = routers.DefaultRouter()
router.register(r'post', views.CartView,'cart'),
urlpatterns = router.urls