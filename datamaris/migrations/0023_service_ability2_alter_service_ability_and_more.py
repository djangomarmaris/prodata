# Generated by Django 4.0.5 on 2022-07-29 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamaris', '0022_service_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='ability2',
            field=models.CharField(default=21, max_length=60, verbose_name='Giriş Yapınız'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='ability',
            field=models.CharField(max_length=60, verbose_name='Giriş Yapınız'),
        ),
        migrations.AlterField(
            model_name='service',
            name='ability3',
            field=models.CharField(max_length=60, verbose_name='Giriş Yapınız'),
        ),
        migrations.AlterField(
            model_name='service',
            name='ability4',
            field=models.CharField(max_length=60, verbose_name='Giriş Yapınız'),
        ),
        migrations.AlterField(
            model_name='service',
            name='ability5',
            field=models.CharField(max_length=60, verbose_name='Giriş Yapınız'),
        ),
        migrations.AlterField(
            model_name='service',
            name='ability6',
            field=models.CharField(max_length=60, verbose_name='Giriş Yapınız'),
        ),
    ]
