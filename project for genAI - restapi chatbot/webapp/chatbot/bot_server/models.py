from django.db import models

# Create your models here.


class Airline(models.Model):
    iata_code = models.CharField(max_length=5)
    airline = models.CharField(max_length=100)


class Airport(models.Model):
    iata_code = models.CharField(max_length=5)
    airport = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=5)
    country = models.CharField(max_length=50)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)


class Flight(models.Model):
    year = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    day = models.IntegerField(null=True, blank=True)
    day_of_week = models.IntegerField(null=True, blank=True)
    airline = models.CharField(max_length=5)
    flight_number = models.IntegerField(null=True, blank=True)
    tail_number = models.TextField(null=True, blank=True)
    origin_airport = models.CharField(max_length=10)
    destination_airport = models.CharField(max_length=10)
    scheduled_departure = models.IntegerField(null=True, blank=True)
    departure_time = models.IntegerField(null=True, blank=True)
    departure_delay = models.IntegerField(null=True, blank=True)
    taxi_out = models.IntegerField(null=True, blank=True)
    wheels_off = models.IntegerField(null=True, blank=True)
    scheduled_time = models.IntegerField(null=True, blank=True)
    elapsed_time = models.IntegerField(null=True, blank=True)
    air_time = models.IntegerField(null=True, blank=True)
    distance = models.IntegerField(null=True, blank=True)
    wheels_on = models.IntegerField(null=True, blank=True)
    taxi_in = models.IntegerField(null=True, blank=True)
    scheduled_arrival = models.IntegerField(null=True, blank=True)
    arrival_time = models.IntegerField(null=True, blank=True)
    arrival_delay = models.IntegerField(null=True, blank=True)
    diverted = models.IntegerField(null=True, blank=True)
    cancelled = models.IntegerField(null=True, blank=True)
    cancellation_reason = models.CharField(max_length=5, null=True, blank=True)
    air_system_delay = models.IntegerField(null=True, blank=True)
    security_delay = models.IntegerField(null=True, blank=True)
    airline_delay = models.IntegerField(null=True, blank=True)
    late_aircraft_delay = models.IntegerField(null=True, blank=True)
    weather_delay = models.IntegerField(null=True, blank=True)

