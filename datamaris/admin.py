from django.contrib import admin
from .models import Comment,Service,Personel,About  ,Referance




class AboutAdmin(admin.ModelAdmin):
    list_display = ['about']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service']


class PersonelAdmin(admin.ModelAdmin):
    list_display = ['name']

class SliderAdmin(admin.ModelAdmin):
    list_display = ['info']


class ReferanceAdmin(admin.ModelAdmin):
    list_display = ['referance']




admin.site.register(About,AboutAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(Personel,PersonelAdmin)
admin.site.register(Referance,ReferanceAdmin)



admin.site.site_header = "Datamaris"

admin.site.index_title = "Developer - İhsan Gürol Demirtaş"

admin.site.site_title = "İGD"