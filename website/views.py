from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def home(request):
    if request.method=="POST":
        contact_Name=request.POST['contactName']
        contact_Email=request.POST['contactEmail']
        contact_Subject=request.POST['contactSubject']
        contact_Message=request.POST['contactMessage']
    
        # send mail
        
        send_mail(
            contact_Subject, #subject
            contact_Message, #message
            contact_Email, #from email 
            ['pururaj2000@gmail.com'] , #to email
            contact_Name, # senders name
            )

        messages.success(request, f' Your mail has been recieved! I will reply you soon.')
        return HttpResponseRedirect("/")

    else:
        return render(request, 'home.html', {})
    
    