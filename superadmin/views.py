from django.shortcuts import render
from .models import State,City,BikeCompany,BikeModel
from django.contrib.auth.decorators import login_required
from .forms import StateForm,CityForm,BikeComapnyForm,BikeModelForm
from .serializer import StateSerializer,CitySerializer,BikeCompanySerializer,BikeModelSerializer
from rest_framework import generics
# Create your views here.


class StateListAPIView(generics.ListAPIView):
	serializer_class 		=		StateSerializer
	queryset				=		State.objects.all()


class CityListAPIView(generics.ListAPIView):
	serializer_class 		=		CitySerializer
	queryset				=		City.objects.all()

class BikeCompanyListAPIView(generics.ListAPIView):
	serializer_class 		=		BikeCompanySerializer
	queryset				=		BikeCompany.objects.all()

class BikeModelListAPIView(generics.ListAPIView):
	serializer_class 		=		BikeModelSerializer
	queryset				=		BikeModel.objects.all()

@login_required(login_url="login")
def state_create(request):
	form 	=	StateForm()
	if request.method=="POST":
		form 	=	StateForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request,'state-create.html',{'form':form})

@login_required(login_url="login")
def city_create(request):
	form 	=	CityForm()
	if request.method=="POST":
		form 	=	CityForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request,'city-create.html',{'form':form})

@login_required(login_url="login")
def bikecompany_create(request):
	form 	=	BikeComapnyForm()
	if request.method=="POST":
		form 	=	BikeComapnyForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request,'bikecompany-create.html',{'form':form})

@login_required(login_url="login")
def bikemodel_create(request):
	form 	=	BikeModelForm()
	if request.method=="POST":
		form 	=	BikeModelForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request,'bikemodel-create.html',{'form':form})


@login_required(login_url="login")
def states(request):
	query 	=	State.objects.all()
	return render(request,'states.html',{'ls':query})

@login_required(login_url="login")
def city(request):
	query 	=	City.objects.all()
	return render(request,'city.html',{'ls':query})

@login_required(login_url="login")
def bikeModel(request):
	query 	=	BikeModel.objects.all()
	return render(request,'bikemodels.html',{'ls':query})

@login_required(login_url="login")
def bikeCompany(request):
	query 	=	BikeCompany.objects.all()
	return render(request,'bikecompany.html',{'ls':query})
