# Generated by Django 3.2.14 on 2022-08-10 06:20

import annoying.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Myplant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('otp_code', models.CharField(max_length=6, null=True, unique=True)),
                ('photo', models.ImageField(blank=True, default='images/chunhello.png', upload_to='images/')),
                ('is_connected', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Plants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('watercycle_spring', models.CharField(max_length=6)),
                ('watercycle_spring_nm', models.CharField(max_length=30)),
                ('watercycle_summer', models.CharField(max_length=6)),
                ('watercycle_summer_nm', models.CharField(max_length=30)),
                ('watercycle_autumn', models.CharField(max_length=6)),
                ('watercycle_autumn_nm', models.CharField(max_length=30)),
                ('watercycle_winter', models.CharField(max_length=6)),
                ('watercycle_winter_nm', models.CharField(max_length=30)),
                ('specl_manage_info', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sensing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remaining_water', models.BooleanField(default=False)),
                ('state_led', models.BooleanField(default=False)),
                ('moisture_level', models.IntegerField(default=0)),
                ('last_watering', models.CharField(blank=True, max_length=16)),
                ('my_plant', annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, to='plants.myplant')),
            ],
        ),
        migrations.AddField(
            model_name='myplant',
            name='plant_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='plants.plants'),
        ),
        migrations.AddField(
            model_name='myplant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000)),
                ('photo', models.ImageField(blank=True, upload_to='images/')),
                ('diary_created_at', models.DateTimeField(auto_now_add=True)),
                ('public_private', models.BooleanField(default=False)),
                ('my_plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plants.myplant')),
            ],
        ),
    ]
