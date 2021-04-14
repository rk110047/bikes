from django.urls import path
# from .views import ReadyBikesAPIView,AllBikesAPIView,vendors,vendor_profile_create,vendor_profile,bike_create,my_bikes,bike_edit
from .views import VendorProfileAPIView,VendorProfileCreateAPIView,ReadyBikesAPIView,AllBikesAPIView,BikeCreateAPIView,MyBikesApiView,BikeRUDAPIView


app_name="vendor"

urlpatterns=[
	# path('list/',vendors,name='vendors'),
	path('create/',VendorProfileCreateAPIView.as_view(),name='vendor-profile-create'),
	path('profile/',VendorProfileAPIView.as_view(),name="vendor-profile"),
	path('all-bikes/',AllBikesAPIView.as_view(),name='all-bikes'),
	path('ready-bikes/',ReadyBikesAPIView.as_view(),name='ready-bikes'),
	path('bike-create/',BikeCreateAPIView.as_view(),name='bike-create'),
	path('my-bikes/',MyBikesApiView.as_view(),name='my-bikes'),
	path('bike-rud/<id>/',BikeRUDAPIView.as_view(),name='bike-rud')
	# path('bike_create/',bike_create,name='bike-create'),
	# path('my-bikes/',my_bikes,name='my-bikes'),
	# path('bike-edit/<id>/',bike_edit,name='bike-edit')
]