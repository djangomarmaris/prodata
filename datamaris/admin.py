from django.contrib import admin
from .models import Comment,Service,Personel,About  ,Referance , Slider , Partners ,Images , YouTube



class Gallery(admin.TabularInline):
    model = Images

class ParthnerAdmin(admin.ModelAdmin):
    list_display = ['title']

class AboutAdmin(admin.ModelAdmin):
    list_display = ['about']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name']

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id','service','title','slug']
    prepopulated_fields = {'slug': ('title',)}
    inlines = (Gallery,)

class PersonelAdmin(admin.ModelAdmin):
    list_display = ['name']

class SliderAdmin(admin.ModelAdmin):
    list_display = ['info']

class ReferanceAdmin(admin.ModelAdmin):
    list_display = ['referance']

class SliderAdmin(admin.ModelAdmin):
    list_display = ['title']

class YouAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(YouTube,YouAdmin)
admin.site.register(Partners,ParthnerAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(Personel,PersonelAdmin)
admin.site.register(Referance,ReferanceAdmin)
admin.site.register(Slider,SliderAdmin)


admin.site.site_header = "Datamaris"

admin.site.index_title = "Developer - İhsan Gürol Demirtaş"

admin.site.site_title = "İGD"