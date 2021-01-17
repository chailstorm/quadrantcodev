from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import post, comment
import datetime as dt
from .forms import blogposts, commentposts
from solutions.models import qinfo
import datetime as dt
# Create your views here.
class blog():
	def mainpage(request):
		filter_kwargs = {
		'status__exact': 1
		}
		posts = post.objects.filter(**filter_kwargs)
		context = {'blogposts': posts}
		return render(request,'blog.html',context=context)
	
	@login_required
	def blogpost(request,bn):
		filter_kwargs = {
		'bn__exact': bn,
		'status__exact': 1
		}
		posts = post.objects.filter(**filter_kwargs)
		comments = comment.objects.filter(**filter_kwargs)
		
		form = commentposts
		if request.method=='POST':
			form = commentposts(data=request.POST)
			if form.is_valid():
				commentpost = form.save(commit=False)
				commentpost.author = request.user.id
				commentpost.status = 1
				commentpost.bn = bn
				try:
					q = qinfo.objects.get(qn=int(request.user.id))
					commentpost.name = q.__str__()
				except Exception:
					c = User.objects.get(id=int(request.user.id))
					commentpost.name = c.first_name + ' ' + c.last_name
				commentpost.save()
				return redirect('blogpost', bn=bn)
		
		now = dt.datetime.now()
		now = now.strftime('%Y-%m-%d')
		context = {
			'blogpost': posts[0],
			'now': now,
			'comments': comments,
			'form': form,
			}
		return render(request,'blogpost.html',context=context)
	
	@login_required
	def create(request):
		form = blogposts
		if request.method=='POST':
			form = blogposts(data=request.POST)
			if form.is_valid():
				blogpost = form.save(commit=False)
				blogpost.author = request.user.id
				blogpost.status = 1
				try:
					q = qinfo.objects.get(qn=request.user.id)
					blogpost.name = q.__str__()
				except Exception:
					c = User.objects.get(id=request.user.id)
					blogpost.name = c.first_name + ' ' + c.last_name
				blogpost.save()
				
				now = dt.datetime.now()
				now = now.strftime('%Y-%m-%d')
				return redirect('account', getq=request.user.id) 
		context = {
			'form': form
			}
		return render(request, 'blogcreate.html', context=context)
	