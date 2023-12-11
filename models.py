from django.db import models
from geopy.geocoders import Nominatim

class District(models.Model):
    DISTRICT_CHOICES = [
        ('Balaka', 'Balaka'),
        ('Blantyre', 'Blantyre'),
        ('Chikwawa', 'Chikwawa'),
        ('Chiradzulu', 'Chiradzulu'),
        ('Chitipa', 'Chitipa'),
        ('Dedza', 'Dedza'),
        ('Dowa', 'Dowa'),
        ('Karonga', 'Karonga'),
        ('Kasungu', 'Kasungu'),
        ('Likoma', 'Likoma'),
        ('Lilongwe', 'Lilongwe'),
        ('Machinga', 'Machinga'),
        ('Mangochi', 'Mangochi'),
        ('Mchinji', 'Mchinji'),
        ('Mulanje', 'Mulanje'),
        ('Mwanza', 'Mwanza'),
        ('Mzimba', 'Mzimba'),
        ('Nkhata Bay', 'Nkhata Bay'),
        ('Nkhotakota', 'Nkhotakota'),
        ('Nsanje', 'Nsanje'),
        ('Ntcheu', 'Ntcheu'),
        ('Ntchisi', 'Ntchisi'),
        ('Phalombe', 'Phalombe'),
        ('Rumphi', 'Rumphi'),
        ('Salima', 'Salima'),
        ('Thyolo', 'Thyolo'),
        ('Zomba', 'Zomba'),
    ]

    name = models.CharField(max_length=100, choices=DISTRICT_CHOICES)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.latitude or not self.longitude:
           
            geolocator = Nominatim(user_agent="core")
            location = geolocator.geocode(self.name + ", Malawi")

            if location:
                self.latitude = location.latitude
                self.longitude = location.longitude

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name



class AirPollutionReading(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    pm25 = models.FloatField()  # Particulate Matter (PM2.5) concentration
    co = models.FloatField()    # Carbon Monoxide (CO) concentration
    no2 = models.FloatField()   # Nitrogen Dioxide (NO2) concentration

    def __str__(self):
        return f"Air Pollution Reading at {self.timestamp} in {self.district}"

class WeatherReading(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    temperature = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()

    def __str__(self):
        return f"Weather Reading at {self.timestamp} in {self.district}"
