# Generated by Django 4.0.5 on 2022-07-28 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamaris', '0019_alter_referance_referance_alter_referance_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service',
            field=models.CharField(max_length=250, verbose_name='Service Hakkında'),
        ),
    ]
