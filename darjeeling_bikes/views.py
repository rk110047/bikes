from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='admin/')
def index(request):
	if request.user.is_superuser:
		return render(request,'home.html',{})
	return render(request,'index2.html',{})