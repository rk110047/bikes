from django.db import models
from superadmin.models import State,City,BikeCompany,BikeModel
from django.contrib.auth import get_user_model
# Create your models here.


User = get_user_model()



class VendorProfile(models.Model):
	user 					=		models.OneToOneField(User,on_delete=models.CASCADE)
	name 					=		models.CharField(max_length=120)
	mobile 					=		models.CharField(max_length=120)
	whatsapp_number 		=		models.CharField(max_length=120)
	email 					=		models.EmailField(unique=True)
	city 					=		models.ForeignKey(City,on_delete=models.CASCADE)
	state 					=		models.ForeignKey(State,on_delete=models.CASCADE)
	photo 					=		models.FileField(upload_to='VendorProfileImages/')
	bank_name 				=		models.CharField(max_length=120)
	bank_account_number 	=		models.CharField(max_length=120)
	ifsc_code 				=		models.CharField(max_length=120)
	branch 					=		models.CharField(max_length=120)


	def __str__(self):
		return self.name


class BikeDetails(models.Model):
	question_choices =(('yes','YES'),('no','NO'))

	vendor 							=		models.ForeignKey(VendorProfile,on_delete=models.CASCADE)
	bike_registraton_number 		=		models.CharField(max_length=120)
	year_of_registration 			=		models.CharField(max_length=120)
	date_of_registration 			=		models.DateField()
	bike_company 					=		models.ForeignKey(BikeCompany,on_delete=models.CASCADE)
	bike_model_name 				=		models.ForeignKey(BikeModel,on_delete=models.CASCADE)
	engine_cc 						=		models.CharField(max_length=120)
	ABS 							=		models.CharField(max_length=120,choices=question_choices)
	tubeless_tyre 					=		models.CharField(max_length=120,choices=question_choices)
	luggage_carrier 				=		models.CharField(max_length=120,choices=question_choices)
	mobiler_holder_and_charger  	=		models.CharField(max_length=120,choices=question_choices)
	color 							=		models.CharField(max_length=120)
	road_tax_validity 				=		models.CharField(max_length=120)
	road_tax_document 				=		models.FileField(upload_to='road_tax_document/')
	pollution_validity 				=		models.CharField(max_length=120)
	pollution_validity_document 	=		models.FileField(upload_to='pollution_validity_document/')
	insurance_validity              =		models.CharField(max_length=120)
	insurance_validity_document 	=		models.FileField(upload_to='insurance_validity_document/')
	registration_validity    		=		models.CharField(max_length=120)
	registration_validity_document 	=		models.FileField(upload_to='registration_validity_document/')
	rent_per_day 					=		models.IntegerField()
	rent_per_day_for_more_than_6_days =		models.IntegerField()
	rent_per_day_for_group 			=		models.IntegerField()
	approved 						=		models.BooleanField(default=False)
	ready 							=		models.BooleanField(default=False)
	already_booked 					=		models.BooleanField(default=False)




	def __str__(self):
		return self.bike_registraton_number

class BikeImages(models.Model):
	bike 				=		models.ForeignKey(BikeDetails,on_delete=models.CASCADE)
	image 				=		models.FileField(upload_to='bike_photos/')

	def __str__(self):
		return self.bike

