from django.urls import path,re_path,include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register(r'groups', GroupsPermissions)
router.register(r'permissions', PermissionsGroups)
urlpatterns = [
	path('',include(router.urls)),
]