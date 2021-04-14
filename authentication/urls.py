from django.urls import path
from .views import LoginWithTokenAuthenticationAPIView,RegisterAPIView,login_user,logout_user

urlpatterns=[
	path('',login_user,name='login'),
	path('logout/',logout_user,name='logout'),
	path('login/',LoginWithTokenAuthenticationAPIView.as_view(),name='login-token'),
	path('register/',RegisterAPIView.as_view(),name='register')
]