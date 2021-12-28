
from django.shortcuts import render

from django.core.mail import send_mail
from django.core.mail import EmailMessage

def index(request):

    return render(request, 'index.html' , {})


def contact(request):
    if request.method == 'POST':
        name = request.POST ['name']
        email = request.POST ['email']
        message1 = request.POST ['message']
        Subject = request.POST ['inquiry']

        #SEND AN EMAIL
        mail_subject =  Subject
        message = message1
        to_email = email
        email1 = EmailMessage(
              mail_subject,  message, to=[to_email]
            )
        email1.send()
        return render(request, 'contact.html',{'name':name})
    else:
        return render(request, 'contact.html',{})


