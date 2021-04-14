from .models import State,City,BikeCompany,BikeModel
from rest_framework import serializers


class StateSerializer(serializers.ModelSerializer):
	class Meta:
		model 		=		State
		fields 		=		'__all__'


class CitySerializer(serializers.ModelSerializer):
	class Meta:
		model 		=		City
		fields 		=		'__all__'


class BikeCompanySerializer(serializers.ModelSerializer):
	class Meta:
		model 		=		BikeCompany
		fields 		=		'__all__'


class BikeModelSerializer(serializers.ModelSerializer):
	class Meta:
		model 		=		BikeModel
		fields 		=		'__all__'