from django.urls import path,include,re_path
from django.conf.urls import url
from rest_framework import permissions
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
	path('schema/', SpectacularAPIView.as_view(), name='schema'),
	# Optional UI:
	path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
	path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
	path('',include('djoser.urls')),
	path('auth/',include('djoser.urls.jwt')),
	path('group/', include('accounts.urls'))
]
