# Generated by Django 4.0.4 on 2022-08-18 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='post_image/'),
        ),
    ]
