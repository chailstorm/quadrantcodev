from django.urls import path
from . import views

urlpatterns = [
	
	path('',views.gotoLogin, name='userlogin'),
	path('error',views.gotoLoginError, name='userloginerror'),
	#path('go',views.goLogin, name='go'),
	path('logout',views.goLogout, name='userlogout'),
	path('register',views.register, name='register'),
	path('qregister/<str:regStr>',views.qregister, name='qregister'),
	path('qupdate',views.qprofileUpdate,name='qupdate'),
	path('cupdate',views.cprofileUpdate,name='cupdate'),
	path('forgotpassword',views.forgotPassword,name='forgotpassword'),
	path('resetpassword/<str:resetStr>',views.resetPassword,name='resetpassword'),
	]
