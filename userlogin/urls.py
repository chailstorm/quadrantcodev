from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

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
	#path('reset_password/',auth_views.PasswordResetView.as_view(),name='reset_password'),
	#path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
	#path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
	#path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
	]
