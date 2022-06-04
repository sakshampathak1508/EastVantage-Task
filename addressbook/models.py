from django.db import models

class Address(models.Model):
    add = models.TextField() #can be anything like house number or shop name or street
    city = models.CharField(max_length=100,blank=True)
    state = models.CharField(max_length=100,blank=True)
    country = models.CharField(max_length=100,blank=True)
    zipcode = models.CharField(max_length=5,blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6,blank=True,null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6,blank=True,null=True)
    coordinates = models.CharField(max_length=50,blank=True)

    def save(self,*args,**kwargs):
        v1 = str(self.latitude)
        v2 = str(self.longitude)
        self.coordinates = v1+', '+v2
        super().save(*args,**kwargs)

    def __str__(self):
        return self.coordinates