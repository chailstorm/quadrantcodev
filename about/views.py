from django.shortcuts import render

# Create your views here.
class about():
	def mainpage(request):
		context = {}
		return render(request,'about.html',context=context)