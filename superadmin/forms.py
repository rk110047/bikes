from django import forms
from .models import State,City,BikeCompany,BikeModel


class StateForm(forms.ModelForm):
	class Meta:
		model 		=		State
		fields 		=		"__all__"

class CityForm(forms.ModelForm):
	class Meta:
		model 		=		City
		fields 		=		"__all__"

class BikeComapnyForm(forms.ModelForm):
	class Meta:
		model 		=		BikeCompany
		fields 		=		"__all__"

class BikeModelForm(forms.ModelForm):
	class Meta:
		model 		=		BikeModel
		fields 		=		"__all__"


