from django.db import models
from vendor.models import BikeDetails
from django.contrib.auth import get_user_model
from .utils import unique_id_generator
from django.db.models.signals import pre_save
# Create your models here.


User = get_user_model()

class CustomerProfile(models.Model):
	user 					=		models.OneToOneField(User,on_delete=models.CASCADE)
	name 					=		models.CharField(max_length=120)
	mobile 					=		models.CharField(max_length=120)
	whatsapp_number 		=		models.CharField(max_length=120)
	email 					=		models.EmailField(unique=True)
	city 					=		models.CharField(max_length=120)
	state 					=		models.CharField(max_length=120)
	photo 					=		models.FileField(upload_to='CustomerProfileImages/')


	def __str__(self):
		return self.name


class MyRides(models.Model):
	Ride_status=(('ongoing','ONGOING'),('completed','COMPLETED'),('canceled','CANCELED'),('upcoming','UPCOMING'))

	ride_id 			   =		models.CharField(max_length=120)
	customer 			   =		models.ForeignKey(CustomerProfile,on_delete=models.CASCADE)
	bike 				   =		models.ForeignKey(BikeDetails,on_delete=models.CASCADE)
	ride_status 		   =		models.CharField(max_length=120,choices=Ride_status)
	start_date 			   =		models.DateField()
	end_date 			   =		models.DateField()
	canceled 			   =		models.BooleanField(default=False)
	review 				   =		models.CharField(max_length=1200)




def pre_save_ride_id_creator(instance,sender,*args,**kwargs):
    if not instance.ride_id:
        instance.ride_id = unique_id_generator(instance)


pre_save.connect(pre_save_ride_id_creator,sender=MyRides)
