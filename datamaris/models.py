from django.db import models

# Create your models here.




class About(models.Model):
    title = models.TextField(max_length=50, verbose_name='Titile')
    about = models.TextField(max_length=300, verbose_name='Hakkımızda Sağ ')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image2 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image3 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image4 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)

    def __str__(self):
        return self.about



class Service(models.Model):
    title = models.CharField(max_length=20, verbose_name='Service title')
    service = models.CharField(max_length=50, verbose_name='Service Hakkında')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)


    def __str__(self):
        return self.service

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








class Referance(models.Model):
    referance = models.CharField(max_length=50, verbose_name='Referance İşletme')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    work = models.CharField(max_length=50, verbose_name='Yapılan İş')


    def __str__(self):
        return self.referance
