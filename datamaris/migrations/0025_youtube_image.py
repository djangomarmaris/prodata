# Generated by Django 4.0.5 on 2022-07-29 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamaris', '0024_youtube'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtube',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
