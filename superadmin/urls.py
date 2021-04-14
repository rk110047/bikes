from django.urls import path
from .views import StateListAPIView,CityListAPIView,BikeCompanyListAPIView,BikeModelListAPIView,state_create,city_create,bikecompany_create,bikemodel_create,states,bikeCompany,bikeModel,city

urlpatterns=[
	path('states/',StateListAPIView.as_view(),name='states'),
	path('city/',CityListAPIView.as_view(),name='city'),
	path('bikemodels/',BikeModelListAPIView.as_view(),name='bikemodels'),
	path('bikecompany/',BikeCompanyListAPIView.as_view(),name='bikecompany'),
	# path('states/',states,name='states'),
	# path('city/',city,name='city'),
	# path('bikemodel/',bikeModel,name='bikemodels'),
	# path('bikecompany/',bikeCompany,name='bikecompany'),
	# path('state-create/',state_create,name='create-state'),
	# path('city-create/',city_create,name='create-city'),
	# path('bikemodel-create',bikemodel_create,name='create-bikemodel'),
	# path('bikecompany-create',bikecompany_create,name='create-bikecompany')

]