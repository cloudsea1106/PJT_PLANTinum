# Generated by Django 3.2.14 on 2022-07-21 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myplant',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='plants.plants'),
        ),
    ]
