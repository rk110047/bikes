from django.urls import path
from .views import CustomerProfileCreateAPIView,CustomerProfileRetrieve,MyRidesAPIView,MyRidesCreateAPIView,customers,ongoing_bookings,upcoming_bookings,completed_bookings,canceled_bookings


urlpatterns=[
	path('ongoing-bookings/',ongoing_bookings,name='ongoing-bookings'),
	path('upcoming-bookings/',upcoming_bookings,name='upcoming-bookings'),
	path('completed-bookings/',completed_bookings,name='completed-bookings'),
	path('canceled-bookings/',canceled_bookings,name='canceled-bookings'),
	path('list/',customers,name='customers'),
	path('profile/create/',CustomerProfileCreateAPIView.as_view(),name='customer-profile-create'),
	path('profile/retrieve/',CustomerProfileRetrieve.as_view(),name='customer-profile-retrieve'),
	path('rides-create/',MyRidesCreateAPIView.as_view(),name='rides-create'),
	path('rides/',MyRidesAPIView.as_view(),name='my-rides-list-create')
]