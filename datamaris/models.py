from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from embed_video.fields import EmbedVideoField

# Create your models here.

class Slider(models.Model):
    title= models.CharField(max_length=200, verbose_name='İlk Yazı')
    header= models.CharField(max_length=200, verbose_name='Kalın Yazı')
    info= models.CharField(max_length=200, verbose_name='Mini Açıklama')
    linkone =  models.CharField(max_length=20, verbose_name='Yönlendirilcek Sayfa 1')
    linktwo = models.CharField(max_length=20, verbose_name='Yönlendirilcek Sayfa 2')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)


    def __str__(self):
        return self.title


class About(models.Model):
    title = models.TextField(max_length=50, verbose_name='Titile')
    about = models.TextField(max_length=1000, verbose_name='Hakkımızda')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    url = EmbedVideoField()


    def __str__(self):
        return self.about



class Service(models.Model):
    title = models.CharField(max_length=20, verbose_name='Service title')
    service = models.CharField(max_length=250, verbose_name='Mini Açıklama')
    header = models.CharField(max_length=500, verbose_name='Başlık')
    info=RichTextUploadingField()
    infoTwo = RichTextUploadingField()
    ability = models.CharField(max_length=60, verbose_name='Giriş Yapınız')
    ability2 = models.CharField(max_length=60, verbose_name='Giriş Yapınız')
    ability3 = models.CharField(max_length=60, verbose_name='Giriş Yapınız')
    ability4 = models.CharField(max_length=60, verbose_name='Giriş Yapınız')
    ability5 = models.CharField(max_length=60, verbose_name='Giriş Yapınız')
    ability6 = models.CharField(max_length=60, verbose_name='Giriş Yapınız')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    slug = models.SlugField(max_length=200, db_index=True)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('datamaris:service_detail', args=[self.slug, self.id])

class Personel(models.Model):
    name = models.CharField(max_length=20, verbose_name='Personel İsim')
    title = models.CharField(max_length=50, verbose_name='Personel title')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    comment = models.TextField(max_length=300, verbose_name='Comment Hakkında')
    name = models.CharField(max_length=50, verbose_name='İsim')
    position = models.CharField(max_length=50, verbose_name='Pozisyon')

    def __str__(self):
        return self.name




class Partners(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    about = models.TextField(max_length=200, verbose_name='Mini Açıkalma 200 ü geçmicek')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)


    def __str__(self):
        return self.title



class Referance(models.Model):
    referance = models.CharField(max_length=50, verbose_name='Referance İşletme')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    work = models.CharField(max_length=50, verbose_name='Yapılan İş')


    def __str__(self):
        return self.referance




class Images(models.Model):
    product=models.ForeignKey(Service,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title


class YouTube(models.Model):
    url = EmbedVideoField()
    image = models.ImageField(blank=True, upload_to='images/')
    name = models.CharField(max_length=50,blank=True)



    def __str__(self):
        return self.name