# Generated by Django 3.0.8 on 2020-08-18 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200818_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='covers/'),
        ),
    ]