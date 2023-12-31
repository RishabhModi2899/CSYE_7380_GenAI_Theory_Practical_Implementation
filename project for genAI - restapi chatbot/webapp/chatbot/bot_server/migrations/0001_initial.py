# Generated by Django 4.2.7 on 2023-11-17 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iata_code', models.CharField(max_length=5)),
                ('airline', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iata_code', models.CharField(max_length=5)),
                ('airport', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=5)),
                ('country', models.CharField(max_length=50)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('day', models.IntegerField()),
                ('day_of_week', models.IntegerField()),
                ('airline', models.CharField(max_length=5)),
                ('flight_number', models.IntegerField()),
                ('tail_number', models.TextField()),
                ('origin_airport', models.CharField(max_length=10)),
                ('destination_airport', models.CharField(max_length=10)),
                ('scheduled_departure', models.IntegerField()),
                ('departure_time', models.IntegerField()),
                ('departure_delay', models.IntegerField()),
                ('taxi_out', models.IntegerField()),
                ('wheels_off', models.IntegerField()),
                ('scheduled_time', models.IntegerField()),
                ('elapsed_time', models.IntegerField()),
                ('air_time', models.IntegerField()),
                ('distance', models.IntegerField()),
                ('wheels_on', models.IntegerField()),
                ('taxi_in', models.IntegerField()),
                ('scheduled_arrival', models.IntegerField()),
                ('arrival_time', models.IntegerField()),
                ('arrival_delay', models.IntegerField()),
                ('diverted', models.IntegerField()),
                ('cancelled', models.IntegerField()),
                ('cancellation_reason', models.CharField(max_length=5)),
                ('air_system_delay', models.IntegerField()),
                ('security_delay', models.IntegerField()),
                ('airline_delay', models.IntegerField()),
                ('late_aircraft_delay', models.IntegerField()),
                ('weather_delay', models.IntegerField()),
            ],
        ),
    ]
