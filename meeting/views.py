from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
class meeting():
	def meet(request):
		context = {}
		return render(request, 'meeting/meeting.html', context)
	

