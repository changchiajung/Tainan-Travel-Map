# Generated by Django 2.1.2 on 2019-03-13 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MapSite',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('site_name', models.CharField(max_length=100)),
                ('location_Id', models.IntegerField(blank=True)),
                ('image', models.FileField(blank=True, upload_to='')),
                ('phone_number', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('site_type', models.CharField(blank=True, max_length=200)),
                ('count', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(blank=True, max_length=20)),
                ('content', models.CharField(blank=True, max_length=1000)),
                ('style', models.CharField(blank=True, max_length=100)),
                ('image', models.FileField(blank=True, upload_to='')),
                ('days', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('day', models.IntegerField()),
                ('sequence', models.IntegerField()),
                ('stay_time', models.IntegerField(blank=True)),
                ('site_content', models.TextField(blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('schedule_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.Schedule')),
                ('site_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.MapSite')),
            ],
        ),
    ]
