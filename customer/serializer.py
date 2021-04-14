from rest_framework import serializers
from .models import CustomerProfile,MyRides
from vendor.serializer import BikeSerializer

class CustomerProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model 		=	CustomerProfile
		fields 		=	"__all__"


class MyRideSerializer(serializers.ModelSerializer):
	bike 		=	BikeSerializer()
	class Meta:
		model 		=	MyRides
		fields 		=	"__all__"
		read_only_fields 	=	['ride_id']

class MyRideCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model 		=	MyRides
		fields 		=	"__all__"
		read_only_fields 	=	['ride_id']