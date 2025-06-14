# Generated by Django 5.2 on 2025-05-22 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('detail', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('dob', models.DateField()),
                ('subscribe', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('profile_pic', models.ImageField(upload_to='image/')),
                ('resume', models.FileField(upload_to='file/')),
                ('password', models.CharField(max_length=55)),
                ('cpassword', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=100, null=True)),
                ('duration', models.CharField(max_length=50, null=True)),
                ('price', models.IntegerField()),
                ('description', models.CharField(null=True)),
                ('itinerary', models.CharField(null=True)),
                ('image', models.ImageField(upload_to='image/')),
                ('inclusions', models.CharField(null=True)),
                ('exclusions', models.CharField(null=True)),
                ('available_from', models.DateField()),
                ('available_to', models.DateField()),
            ],
        ),
    ]
