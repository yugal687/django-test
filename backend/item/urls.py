from django.urls import path
from . import views
from rest_framework import routers
from django.urls import include, path
#users
# from .views import current_user, UserList  

router = routers.DefaultRouter()
router.register(r'post', views.ItemView,'item'),
urlpatterns = router.urls

# urlpatterns = [
# path('auth/', include('rest_auth.urls')),    
# path('auth/register/', include('rest_auth.registration.urls'))
# ]
#users
# urlpatterns += [
#     path('current_user/', current_user),
#     path('users/', UserList.as_view())
# ]