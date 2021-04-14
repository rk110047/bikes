from django.shortcuts import render
from rest_framework.response import Response
from .serializer import BikeSerializer,VendorProfileSerializer,BikeCreateSerializer
from rest_framework import generics
from .models import VendorProfile,BikeDetails,BikeImages
from django.contrib.auth.decorators import login_required
from .forms import VendorProfileForm,BikeForm,VendorProfileCreateForm


# Create your views here.



class VendorProfileAPIView(generics.GenericAPIView):
	serializer_class 	=	VendorProfileSerializer
	queryset 			=	VendorProfile.objects.all()

	def get(self,request):
		user 		=	self.request.user
		query 		=	VendorProfile.objects.get(user=user)
		serialize 	=	VendorProfileSerializer(query)
		return Response(serialize.data)

class VendorProfileCreateAPIView(generics.CreateAPIView):
	serializer_class 	=	VendorProfileSerializer
	queryset 			=	VendorProfile.objects.all()

	def perform_create(self,serializer):
		user 	=	self.request.user
		serializer.save(user=user)


class ReadyBikesAPIView(generics.ListAPIView):
	serializer_class 		=		BikeSerializer
	def get_queryset(self):
		query 		=		BikeDetails.objects.filter(approved=True,ready=True)
		return query




class AllBikesAPIView(generics.ListAPIView):
	serializer_class 		=		BikeSerializer
	def get_queryset(self):
		query 		=		BikeDetails.objects.filter(approved=True)
		return query


class BikeCreateAPIView(generics.CreateAPIView):
	serializer_class 		=	BikeCreateSerializer
	query 					=	BikeDetails.objects.all()



	def perform_create(self,serializer):
		vendor 		=		self.request.user.vendorprofile
		serializer.save(vendor=vendor)

class MyBikesApiView(generics.ListAPIView):
	serializer_class 		=		BikeSerializer
	queryset 				=		BikeDetails.objects.all()


	def get(self,request):
		user 		=		self.request.user
		vendor 		=		user.vendorprofile
		query 		=		BikeDetails.objects.filter(vendor=vendor)
		serialize 	=		BikeSerializer(query,many=True,context={'request':request})
		return Response(serialize.data)

class BikeRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class 		=		BikeCreateSerializer
	queryset 				=		BikeDetails.objects.all()
	lookup_field 			=		"id"




# @login_required(login_url="login")
# def vendors(request):
# 	query 	=	VendorProfile.objects.all()
# 	return render(request,'vendors.html',{'ls':query})



# @login_required(login_url="login")
# def vendor_profile_create(request):
# 	form 	=	VendorProfileCreateForm()
# 	if request.method=="POST":
# 		form 	=		VendorProfileCreateForm(request.POST,request.FILES)
# 		print(form.is_valid())
# 		if form.is_valid():
# 			form.save()
# 	return render(request,'vendor-profile-create.html',{'form':form})



# @login_required(login_url="login")
# def vendor_profile(request):
# 	user 	=	request.user
# 	query 	=	VendorProfile.objects.get(user=user)
# 	form 	=	VendorProfileForm(instance=query)
# 	if request.method=="POST":
# 		form 	=		VendorProfileForm(request.POST,request.FILES,instance=query)
# 		print(form.is_valid())
# 		if form.is_valid():
# 			form.save()
# 	return render(request,'vendor-profile.html',{'obj':query,'form':form})

# @login_required(login_url="login")
# def bike_create(request):
# 	vendor 	=	request.user.vendorprofile.id
# 	form 	=	BikeForm()
# 	if request.method=="POST":
# 		form 	=	BikeForm(request.POST,request.FILES)
# 		if form.is_valid():
# 			form.vendor = vendor
# 			form.save()
# 	return render(request,'bike-create.html',{'form':form})

# @login_required(login_url="login")
# def my_bikes(request):
# 	vendor 	=	request.user.vendorprofile.id
# 	query 	=	BikeDetails.objects.filter(vendor=vendor)
# 	return render(request,'my-bikes.html',{'ls':query})


# @login_required(login_url="login")
# def bike_edit(request,id=None):
# 	vendor 	=	request.user.vendorprofile.id
# 	bike 	=	BikeDetails.objects.get(id=id)
# 	form 	=	BikeForm(instance=bike)
# 	if request.method=="POST":
# 		form 	=	BikeForm(request.POST,request.FILES,instance=bike)
# 		if form.is_valid():
# 			form.save()
# 	return render(request,'bike-edit.html',{'form':form})
