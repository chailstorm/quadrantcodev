from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import contactUs
from django.core import mail
from solutions.models import qinfo

# Create your views here.
class contact():
    def us(request,qid):
        form = contactUs
        if request.method=='POST':
            form = contactUs(data=request.POST)
            if form.is_valid():             
                contact = form.save(commit=False)
                name = form.cleaned_data.get('name')
                email = form.cleaned_data.get('email')
                comment =  form.cleaned_data.get('comment')
                
                contact.directed = qid
                contact.contactEmail = 1
                contact.save()
                """
                subject = 'Contact Request from ' + name
                plain_message = 'Sent on behalf of ' + email + '\n' + comment
                
                if qid==0:
                    to_email = ('coltonjameshail@gmail.com',)
                else:
                    filter_kwargs = {
                    'qn__exact': qid,
                    }
                    q = qinfo.objects.filter(**filter_kwargs)
                    to_email = (q[0].email,)
                mail.send_mail(subject,plain_message,'',to_email,html_message=None)
                """
                
                messages.success(request, "Thank you for your message! We will get back to you shortly.")
                
            else:
                messages.error(request, "Please fill out all forms.")
                
        else:
            if qid!=0:
                messages.info(request, 'Please fill out the form below. ' + qinfo.objects.get(qn=qid).__str__() + ' will respond shortly')
        context = {
            'form': form,
            'qid': qid
            }
        return render(request, 'contact.html', context)
    
    def enterprise(request):
        messages.info(request,'Let us know how we can help your organization and our enterprise team will reach out shortly.')
        return redirect('contact', qid=0)
        
    def rush(request):
        messages.info(request,'RUSH REQUEST: please provide a description of how we can help you and our action team will contact you within a few hours.')
        return redirect('contact', qid=0)