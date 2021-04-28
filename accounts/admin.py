from django.contrib import admin
from .models import *
# Register your models here.
class UserAdmin(auth_admin.UserAdmin):
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		('Personal info', {'fields': ('first_name', 'last_name', 'photo')}),
		('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser','groups', 'user_permissions')}),
		('Important dates', {'fields': ('last_login', 'date_joined')}),
	)
	limited_fieldsets = (
		(None, {'fields': ('email',)}),
		('Personal info', {'fields': ('first_name', 'last_name', 'photo')}),
		('Important dates', {'fields': ('last_login', 'date_joined')}),
	)
	add_fieldsets = (
		(None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
		),
	)