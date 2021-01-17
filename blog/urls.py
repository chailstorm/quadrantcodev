from django.urls import path
from . import views

urlpatterns = [
	path('',views.blog.mainpage, name='blog'),
	path('post/<int:bn>',views.blog.blogpost, name='blogpost'),
	path('create',views.blog.create, name='create')
	]
