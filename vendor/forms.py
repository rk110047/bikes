from django import forms
from .models import VendorProfile,BikeDetails,BikeImages



class VendorProfileForm(forms.ModelForm):
	class Meta:
		model 		=	VendorProfile
		fields 		=	"__all__"
		exclude 	=	['user']


class VendorProfileCreateForm(forms.ModelForm):
	class Meta:
		model 		=	VendorProfile
		fields 		=	"__all__"


class BikeForm(forms.ModelForm):
	class Meta:
		model 		=	BikeDetails
		fields 		=	"__all__"
		exclude 	=	['vendor','approved','already_booked',]