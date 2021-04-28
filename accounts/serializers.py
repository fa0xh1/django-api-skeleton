from django.contrib.auth.models import Group,Permission
from django.core import exceptions as django_exceptions
from django.contrib.auth.password_validation import validate_password
from django.db import IntegrityError, transaction
from rest_framework import serializers
from django.contrib.auth import get_user_model
from djoser.conf import settings
from .models import *

class UserSerializer(serializers.ModelSerializer):
	full_name = serializers.CharField(source='get_full_name',required=False,read_only=True)
	password = serializers.CharField(style={"input_type": "password"}, write_only=True,required=False)
	avatar = serializers.ImageField(required=False)
	group_name = serializers.SerializerMethodField('get_groups',read_only=True)
	
	def get_groups(self, obj):
		return obj.groups.values_list('name', flat=True)
	
	class Meta:
		ref_name = 'AccountsSerializer'
		model = User
		fields = ('username','email','password','user_permissions','group_name','groups','first_name','last_name','full_name','is_active','is_staff','is_superuser','avatar','date_joined')
 	
	def update(self, instance, validated_data):
		user = super().update(instance, validated_data)
		try:
			user.set_password(validated_data['password'])
			user.save()
		except KeyError:
			pass
		return user

class MeSerializer(serializers.ModelSerializer):
	full_name = serializers.CharField(source='get_full_name',required=False,read_only=True)
	password = serializers.CharField(style={"input_type": "password"}, write_only=True,required=False)
	
	class Meta:
		model = User
		fields = ('username','email','first_name','last_name','full_name','avatar','password','date_joined')		
		
	def update(self, instance, validated_data):
		user = super().update(instance, validated_data)
		try:
			user.set_password(validated_data['password'])
			user.save()
		except KeyError:
			pass
		return user

class UserCreateSerializer(serializers.ModelSerializer):
	password = serializers.CharField(style={"input_type": "password"}, write_only=True)

	default_error_messages = {
		"cannot_create_user": settings.CONSTANTS.messages.CANNOT_CREATE_USER_ERROR
	}

	class Meta:
		model = User
		fields = tuple(User.REQUIRED_FIELDS) + (
			settings.LOGIN_FIELD,
			settings.USER_ID_FIELD,
			"password",
		)

	def validate(self, attrs):
		user = User(**attrs)
		password = attrs.get("password")

		try:
			validate_password(password, user)
		except django_exceptions.ValidationError as e:
			serializer_error = serializers.as_serializer_error(e)
			raise serializers.ValidationError(
				{"password": serializer_error["non_field_errors"]}
			)

		return attrs

	def create(self, validated_data):
		try:
			user = self.perform_create(validated_data)
		except IntegrityError:
			self.fail("cannot_create_user")

		return user

	def perform_create(self, validated_data):
		with transaction.atomic():
			user = User.objects.create_user(**validated_data)
			if settings.SEND_ACTIVATION_EMAIL:
				user.is_active = False
				user.save(update_fields=["is_active"])
		return user

class GroupsPermissionsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = "__all__"
class PermissionsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Permission
		fields = "__all__"