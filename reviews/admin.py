from django.contrib import admin
from . import models


# Register your models here.



@admin.register(models.Reviews)
class ReviewAdmin(admin.ModelAdmin) : 
    list_display = ("__str__", "rating_average")