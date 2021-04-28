from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class PermissionUser(permissions.BasePermission):
	message = {'message': ["You don't have permission"]}
	
	def has_object_permission(self, request, view, obj):
		if view.action == 'list':
			return obj == request.user or request.user.has_perm('accounts.view_user')
		elif view.action == 'create':
			return obj == request.user or request.user.has_perm('accounts.add_user')
		elif view.action in ['update', 'partial_update']:
			return obj == request.user or request.user.has_perm('accounts.change_user')
		elif view.action == 'destroy':
			return obj == request.user or request.user.has_perm('accounts.delete_user')

"""
if you want to use has_permission

def has_permission(self, request, view):
	if view.action == 'list':
		if not request.user.has_perm('accounts.view_user'):
			return False
			# raise PermissionDenied({"message":"You don't have permission"})
		return True
	elif view.action == 'create':
		if not request.user.has_perm('accounts.add_user'):
			return False
			# raise PermissionDenied({"message":"You don't have permission"})
		return True        
	elif view.action in ['update', 'partial_update']:
		if not request.user.has_perm('accounts.change_user'):
			return False
			#  raise PermissionDenied({"message":"You don't have permission"})
		return True
	elif view.action == 'destroy':
		if not request.user.has_perm('accounts.delete_user'):
			return False
			#  raise PermissionDenied({"message":"You don't have permission"})
		return True
"""