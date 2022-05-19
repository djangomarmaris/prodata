from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from .models import Service,About,Personel,Comment ,Referance
# Create your views here.


def index(request):
    abouts = About.objects.all()
    services = Service.objects.all()
    personels = Personel.objects.all()
    referances = Referance.objects.all()
    comments = Comment.objects.all()

    context = {
        'abouts':abouts,
        'services':services,
        'personels':personels,
        'referances':referances,
        'comments':comments
    }

    return render(request,'central/index.html',context)


def service(request):
    services = Service.objects.all()


    context = {
       'services':services
    }
    return render(request,'central/service.html',context)


def referance(request):
    referances = Referance.objects.all()


    context = {
        'referances':referances
    }
    return render(request,'central/referance.html',context)

def contact(request):
    if 'btnSubmit' in request.POST:
        if True:
            nerden= 'iletişim formu mesajı'
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            subjects = request.POST.get('subject')
            messages = request.POST.get('messages')

            subject = 'Contact Page Costumer Back'
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email,"djangomarmaris@gmail.com"]
            contact_message = "\nName:%s\nEmail:%s\nSubject:%s\nPhone:%s\nmessages:%s" % (
                name,
                email,
            phone,
            subjects,
            messages)
            send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
            return redirect('/')
    return render(request,'central/contact.html')