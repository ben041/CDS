from django.db import models
from geopy.geocoders import Nominatim

# Create your models here.


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



class CholeraDatabase(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    cases = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    cured = models.IntegerField(default=0)

    hospitalised = models.IntegerField(default=0)
    description = models.CharField(max_length=255, blank=True, null=True)
    
    


