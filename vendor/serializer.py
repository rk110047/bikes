from rest_framework import serializers
from .models import VendorProfile,BikeDetails,BikeImages
from superadmin.serializer import StateSerializer,CitySerializer,BikeCompanySerializer,BikeModelSerializer




class BikeSerializer(serializers.ModelSerializer):
	rud 							=		serializers.HyperlinkedIdentityField(view_name="vendor:bike-rud",lookup_field="id")
	bike_company 					=		BikeCompanySerializer()
	bike_model_name 				=		BikeModelSerializer()
	class Meta:
		model  		=		BikeDetails
		fields 		=	"__all__"

class BikeCreateSerializer(serializers.ModelSerializer):
	
	class Meta:
		model  		=		BikeDetails
		fields 		=	"__all__"
		read_only_fields	=	['vendor']

class VendorProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model 		=	VendorProfile
		fields 		=		"__all__"
		read_only_fields =	['user']