from rest_framework import viewsets
from rest_framework import status
from .serializers import *
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group,Permission
from rest_framework.permissions import BasePermission

User = get_user_model()

def permission_required(permission_name, raise_exception=False):
	class PermissionRequired(BasePermission):
		message = {'message': ["You don't have permission"]}
		def has_permission(self, request, view):
			if not request.user.has_perm(permission_name):
				return False
			return True
	return PermissionRequired

class GroupsPermissions(viewsets.ModelViewSet):
	#permission_classes = (permission_required("auth.view_group", raise_exception=True),)
	queryset = Group.objects.all()
	serializer_class = GroupsPermissionsSerializer

	def get_permissions(self):
		permission_classes = ()
		if self.action == 'create':
			permission_classes = (permission_required("auth.add_group", raise_exception=True),)
		elif self.action == 'list':
			permission_classes = (permission_required("auth.view_group", raise_exception=True),)
		elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
			permission_classes = (permission_required("auth.change_group", raise_exception=True),)
		elif self.action == 'destroy':
			permission_classes = (permission_required("auth.delete_group", raise_exception=True),)
		return [permission() for permission in permission_classes]

class PermissionsGroups(viewsets.ModelViewSet):
	queryset = Permission.objects.all()
	serializer_class = PermissionsSerializer

	def get_permissions(self):
		permission_classes = ()
		if self.action == 'create':
			permission_classes = (permission_required("auth.add_permission", raise_exception=True),)
		elif self.action == 'list':
			permission_classes = (permission_required("auth.view_permission", raise_exception=True),)
		elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
			permission_classes = (permission_required("auth.change_permission", raise_exception=True),)
		elif self.action == 'destroy':
			permission_classes = (permission_required("auth.delete_permission", raise_exception=True),)
		return [permission() for permission in permission_classes]
