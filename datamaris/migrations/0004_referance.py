# Generated by Django 4.0.2 on 2022-05-15 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamaris', '0003_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Service title')),
                ('referance', models.CharField(max_length=50, verbose_name='Service Hakkında')),
                ('image', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
            ],
        ),
    ]
