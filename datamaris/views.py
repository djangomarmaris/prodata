from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from .models import Service, About, Personel, Comment, Referance, Slider, Partners, Images , YouTube


# Create your views here.


def index(request):
    partners = Partners.objects.all()
    sliders = Slider.objects.all()
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
        'comments':comments,
        'sliders':sliders,
        'partners':partners
    }

    return render(request,'central/index.html',context)


def service(request):
    partners = Partners.objects.all()
    sliders = Slider.objects.all()
    abouts = About.objects.all()
    services = Service.objects.all()
    personels = Personel.objects.all()
    referances = Referance.objects.all()
    comments = Comment.objects.all()

    context = {
        'abouts': abouts,
        'services': services,
        'personels': personels,
        'referances': referances,
        'comments': comments,
        'sliders': sliders,
        'partners': partners
    }
    return render(request,'central/service.html',context)


def service_detail(request,slug,id):
    partners = Partners.objects.all()
    sliders = Slider.objects.all()
    abouts = About.objects.all()
    services = Service.objects.all()
    personels = Personel.objects.all()
    referances = Referance.objects.all()
    comments = Comment.objects.all()

    product = get_object_or_404(Service, slug=slug,id=id)
    images = Images.objects.filter(product_id=id)

    context = {
        'abouts': abouts,
        'services': services,
        'personels': personels,
        'referances': referances,
        'comments': comments,
        'sliders': sliders,
        'partners': partners,
        'product':product,
        'images':images
    }
    return render(request,'central/service_detail.html',context)


def referance(request):
    partners = Partners.objects.all()
    sliders = Slider.objects.all()
    abouts = About.objects.all()
    services = Service.objects.all()
    personels = Personel.objects.all()
    referances = Referance.objects.all()
    comments = Comment.objects.all()

    context = {
        'abouts': abouts,
        'services': services,
        'personels': personels,
        'referances': referances,
        'comments': comments,
        'sliders': sliders,
        'partners': partners
    }
    return render(request,'central/referance.html',context)

def contact(request):
    videos = YouTube.objects.all()
    partners = Partners.objects.all()
    sliders = Slider.objects.all()
    abouts = About.objects.all()
    services = Service.objects.all()
    personels = Personel.objects.all()
    referances = Referance.objects.all()
    comments = Comment.objects.all()

    context = {
        'abouts': abouts,
        'services': services,
        'personels': personels,
        'referances': referances,
        'comments': comments,
        'sliders': sliders,
        'partners': partners,
        'videos': videos
    }
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
    return render(request,'central/contact.html',context)




def video(request):
    videos = YouTube.objects.all()
    partners = Partners.objects.all()
    sliders = Slider.objects.all()
    abouts = About.objects.all()
    services = Service.objects.all()
    personels = Personel.objects.all()
    referances = Referance.objects.all()
    comments = Comment.objects.all()

    context = {
        'abouts': abouts,
        'services': services,
        'personels': personels,
        'referances': referances,
        'comments': comments,
        'sliders': sliders,
        'partners': partners,
        'videos':videos
    }
    return render(request,'central/video.html',context)