from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.

@admin.register(models.User)
class CustomUserAdmin(UserAdmin): 
    """Custom User Admin"""


    fieldsets =  UserAdmin.fieldsets + (
            (
                "Custom profile",
                {
                    "fields": (
                        "avatar",
                        "gender",
                        "bio",
                        "birthdata",
                        "langauge",
                        "currency",
                        "superhost"
                                                
                    )
                },
            ),
        )

    list_filter = UserAdmin.list_filter + ("superhost" , )

    list_display = (
          "username" , 
          "first_name" , 
          "last_name", 
          "email",
          "is_active", 
          "langauge", 
          "currency", 
          "superhost", 
          "is_staff", 
          "is_superuser",
        )