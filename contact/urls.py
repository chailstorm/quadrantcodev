from django.urls import path
from . import views

urlpatterns = [
	path('<int:qid>',views.contact.us,name='contact'),
	path('enterprise',views.contact.enterprise,name='contactEnterprise'),
	path('rush',views.contact.rush,name='contactRush')
]