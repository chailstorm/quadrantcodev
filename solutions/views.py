from django.shortcuts import render
from solutions.models import qinfo
import datetime as dt
#import requests
# Create your views here

def solutions(request):
	context = {
		'servicelinedev': 'servicelinedev',
		'capitalplan': 'capitalplan',
		'pysicianrecruitment': 'pysicianrecruitment',
		'processimprove': 'processimprove',
		'productivity': 'productivity',
		'operationsfinance': 'operationsfinance',
		'leadingmeetings': 'leadingmeetings',
		'dataanalysis': 'dataanalysis',
		'teamcourses': 'teamcourses',
		'personalleadership': 'personalleadership',
		'personalitytypes': 'personalitytypes',
		'tempassignments': 'tempassignments',
		}
	return render(request, 'solutions.html', context=context)

class qsearch():
	model = qinfo
	template_name = 'qlist.html'
	#FUTURE paginiate_by = 20
	queryset = qinfo.objects.filter()
	
	def get_search(request, subcat):
		filter_kwargs = {
			subcat + '__contains': 1,
			'active__exact': 1
			}
		qs = qinfo.objects.filter(**filter_kwargs)
		now = dt.datetime.now()
		now = now.strftime('%Y-%m-%d')
		context = {
			'qs': qs,
			'now': now
			}
		return render(request, 'qlist.html', context=context)
	
	def strsearch(request):
		queries = request.GET.get('searchfield').split()
		results = qinfo.objects.none()
		for query in queries:
			filter_kwargs = {
				'special1__icontains': query,
				'active__exact': 1
				}
			result1 = qinfo.objects.filter(**filter_kwargs)
			
			filter_kwargs = {
				'special2__icontains': query,
				'active__exact': 1
				}
			result2 = qinfo.objects.filter(**filter_kwargs)
			
			filter_kwargs = {
				'special3__icontains': query,
				'active__exact': 1
				}
			result3 = qinfo.objects.filter(**filter_kwargs)
			
			filter_kwargs = {
				'special4__icontains': query,
				'active__exact': 1
				}
			result4 = qinfo.objects.filter(**filter_kwargs)
			
			filter_kwargs = {
				'special5__icontains': query,
				'active__exact': 1
				}
			result5 = qinfo.objects.filter(**filter_kwargs)
			
			filter_kwargs = {
				'description__icontains': query,
				'active__exact': 1
				}
			resultD = qinfo.objects.filter(**filter_kwargs)
			
			filter_kwargs = {
				'bio__icontains': query,
				'active__exact': 1
				}
			resultB = qinfo.objects.filter(**filter_kwargs)
			
			filter_kwargs = {
				'first__icontains': query,
				'active__exact': 1
				}
			resultF = qinfo.objects.filter(**filter_kwargs)
			
			filter_kwargs = {
				'last__icontains': query,
				'active__exact': 1
				}
			resultL = qinfo.objects.filter(**filter_kwargs)
		
			result = result1 | result2 | result3 | result4 | result5 | resultD | resultB | resultF | resultL
			results = results | result
		
		now = dt.datetime.now()
		now = now.strftime('%Y-%m-%d')
		context = {
			'qs': results,
			'now': now
			}
		return render(request, 'qlist.html', context=context)

	def allqs():
		queryset = qinfo.objects.filter(active=1)
		return queryset

	def qlist(request):
		qs = qsearch.allqs()
		now = dt.datetime.now()
		now = now.strftime('%Y-%m-%d')
		context = {
			'qs': qs,
			'now': now
			}
		return render(request, 'qlist.html', context=context)
	

		
