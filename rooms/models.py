


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
      pass


class Amenity(AbstractItem) : 
        pass


class Facility(AbstractItem) :
    """Facility Model Deifinition"""



class Rule(AbstractItem) : 
     pass


class HouseRule(AbstractItem) : 
    pass



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
    chek_in = models.TimeField()
    chek_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User , on_delete=models.CASCADE)
    room_type = models.ManyToManyField(RoomType, on_delete=models.SET_NULL, null=True)

    amenities = models.ManyToManyField(Amenity) 
    
    def __str__(self) : 
        return self.name

    