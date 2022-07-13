


from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models

# Create your models here.

class AbstractItem(core_models.TimeStampedModel) : 
    """Abstract Item"""

    name = models.CharField(max_length = 80)

    class Meta : 
        abstract = True 

    def __str__(self) : 
        return self.name



class RoomType(AbstractItem) : 
    class meta:

        verbose_name_plural = "Room Types"
        



class Amenity(AbstractItem) : 
    
    class meta : 

        verbose_name_plural = "Amenities"


class Facility(AbstractItem) :
    """Facility Model Deifinition"""
    
    class meta : 

        verbose_name_plural = "Facility"




class Rule(AbstractItem) : 
     pass


class HouseRule(AbstractItem) : 
    class meta:

        verbose_name_plural = "House Rule"




class Room(models.Model) : 
    """Room Model Definition"""


    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField(null=True)
    beds = models.IntegerField(null=True)
    bedrooms = models.IntegerField(null=True)
    baths = models.IntegerField(null=True)
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User , on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    facilities = models.ManyToManyField(Facility)
    house_rules = models.ManyToManyField(HouseRule)
    amenities = models.ManyToManyField(Amenity) 
    
    def __str__(self) : 
        return self.name

    