from django.urls import path
from . import views

urlpatterns = [
	path('',views.solutions,name='solutions'),
	path('qlist/',views.qsearch.qlist,name='qlist'),
	path('qsearch/<str:subcat>',views.qsearch.get_search,name='qsearchfunc'),
	path('search/',views.qsearch.strsearch,name='search'),
]