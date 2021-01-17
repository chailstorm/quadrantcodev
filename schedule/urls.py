from django.urls import path
from . import views

urlpatterns = [
	path('schedule/<int:qid>/<int:year>/<int:month>/<int:day>/<str:start>/<str:end>',views.scheduler.confirm,name='schedule'),
	path('checkout/<int:qid>/<int:year>/<int:month>/<int:day>/<str:start>/<str:end>',views.checkout.payment,name='checkout'),
	path('checkout/create-payment-intent',views.checkout.createpayment, name='create-payment-intent'),
	path('checkout/payment-complete',views.checkout.paymentcomplete, name='payment-complete'),
	path('cancel/<int:uid>/<int:year>/<int:month>/<int:day>/<str:start>',views.scheduler.cancel,name='cancel'),
	path('forward/<int:qid>/<int:year>/<int:month>/<int:day>/<str:start>',views.scheduler.forward,name='forward'),
]