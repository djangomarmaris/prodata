from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views


app_name = 'datamaris'


urlpatterns =[

    path('',views.index,name ='index'),
    path('referance/',views.referance,name='referance'),
    path('service/',views.service,name='service'),
    path('contact/',views.contact,name='contact'),
    path('video/',views.video,name='video'),
    path('<str:slug>/<int:id>/',views.service_detail,name='service_detail')

]
