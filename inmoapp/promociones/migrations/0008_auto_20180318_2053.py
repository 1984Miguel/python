# Generated by Django 2.0.3 on 2018-03-18 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promociones', '0007_auto_20180318_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='promocion',
            name='dormitorios',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='promocion',
            name='precio',
            field=models.IntegerField(blank=True, max_length=150, null=True),
        ),
    ]
