from django.urls import path
from . import views

urlpatterns = [
	path('meeting/<str:uname>/<str:mn>/<str:mp>',views.joinmeeting.join)
]