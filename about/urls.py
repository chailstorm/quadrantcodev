from django.urls import path
from . import views

urlpatterns = [
	path('',views.about.mainpage,name='about'),
]