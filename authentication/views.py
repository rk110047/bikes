from django.shortcuts import render,redirect
from .serializer import LoginSerializer,RegisterSerializer
from rest_framework import generics,mixins,status
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,get_user_model,logout
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.authtoken.models import Token


User = get_user_model()

class LoginWithTokenAuthenticationAPIView(generics.GenericAPIView):
    serializer_class    =       LoginSerializer
    permission_classes     =   []
    authentication_classes =   []

    def post(self,request):
        print(request.data)
        username    =   request.data.get('mobile')
        print(username)
        user        =   User.objects.get(username=str(username))
        print(user)
        if user is not None:
            # login(user,request)
            #TOKEN STUFF
            token, _ = Token.objects.get_or_create(user = user)
            login(request,user)
            #token_expire_handler will check, if the token is expired it will generate new one
            # is_expired, token = token_expire_handler(token)     # The implementation will be described further

            return Response({ 
                'token': token.key,
            }, status=status.HTTP_200_OK)
        response = {
        "data": {
            "message": "Your login information is invalid",
            "status": "invalid"
        }
    }
        return Response(response, status=status.HTTP_200_OK)


class RegisterAPIView(generics.CreateAPIView):
     queryset               =   User.objects.all()
     permission_classes     =   []
     authentication_classes =   []
     serializer_class       =   RegisterSerializer

     def post(self,request,*args,**kwargs):
        username   =   request.data.get('mobile')
        email      =   request.data.get('email')
        user       =    User.objects.create_user(username=username,email=email)
        user       =	User.objects.get(username=username)
        if user is not None:
        	token, _ = Token.objects.get_or_create(user = user)
        	return Response({ 
            'token': token.key,
          }, status=status.HTTP_200_OK)
        return Response({'message':'invalid form'})


def login_user(request):
	if request.method=="POST":
		username		=	request.POST['mobile']
		try:
			user        	=   User.objects.get(username=str(username))
			login(request,user)
			return redirect('index')
		except:
			return render(request,'login.html',{})
	return render(request,'login.html',{})


def logout_user(request):
	logout(request)
	return redirect('login')