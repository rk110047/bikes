from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import CustomerProfileSerializer,MyRideSerializer,MyRideCreateSerializer
from .models import CustomerProfile,MyRides
from django.contrib.auth.decorators import login_required

# Create your views here.


class CustomerProfileCreateAPIView(generics.CreateAPIView):
	serializer_class 		=	CustomerProfileSerializer
	queryset 				=	CustomerProfile.objects.all()



class CustomerProfileRetrieve(generics.GenericAPIView):
	serializer_class 	=		CustomerProfileSerializer
	queryset 			=		CustomerProfile.objects.all()

	def get(self,request):
		print(self.request.user)
		query 		=		self.request.user.customerprofile
		serialize 	=		CustomerProfileSerializer(query)
		return 	Response(serialize.data)



class MyRidesCreateAPIView(generics.CreateAPIView):
	serializer_class	=	MyRideCreateSerializer
	queryset 			=	MyRides.objects.all()

	def post(self,request,*args,**kwargs):
		return self.create(request,*args,**kwargs)

	def perform_create(self,serializer):
		customer 	=	self.request.user.customerprofile
		serializer.save(customer=customer)



class MyRidesAPIView(generics.ListAPIView):
	serializer_class	=	MyRideSerializer
	queryset 			=	MyRides.objects.all()

	def get(self,request):
		request 	=		self.request
		status 		=		self.request.GET.get('status')
		customer 	=		request.user.customerprofile
		query 		=		MyRides.objects.filter(customer=customer,ride_status=status)
		serialize 	=		MyRideSerializer(query,many=True)
		return Response(serialize.data)


@login_required(login_url="login")
def customers(request):
	query 	=	CustomerProfile.objects.all()
	return render(request,'customers.html',{'ls':query})

@login_required(login_url="login")
def ongoing_bookings(request):
	query 		=		MyRides.objects.filter(ride_status='ongoing')
	return render(request,'bookings.html',{'ls':query})

@login_required(login_url="login")
def upcoming_bookings(request):
	query 		=		MyRides.objects.filter(ride_status='upcoming')
	return render(request,'bookings.html',{'ls':query})

@login_required(login_url="login")
def canceled_bookings(request):
	query 		=		MyRides.objects.filter(ride_status='canceled')
	return render(request,'bookings.html',{'ls':query})

@login_required(login_url="login")
def completed_bookings(request):
	query 		=		MyRides.objects.filter(ride_status='completed')
	return render(request,'bookings.html',{'ls':query})


