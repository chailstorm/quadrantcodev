from django.urls import path
from . import views
#app_name = 'profiles'
urlpatterns = [
	path('profiles/<str:getq>/<str:availstart>',views.qprofile.get_q,name='profiles'),
	path('account/<str:getq>',views.qprofile.account,name='account'),
	path('availability/<str:getq>/<str:availstart>',views.qprofile.setAvail,name='availability')
]