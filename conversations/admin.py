from django.contrib import admin
from . import models


# Register your models here.


@admin.register(models.Messeage)
class MessageAdmin(admin.ModelAdmin) : 
   
    list_display = ("__str__", "created")
   


@admin.register(models.Conversation)
class ConversationAdmoin(admin.ModelAdmin) : 
    
    
    list_display = ("__str__" , "count_messages" , "count_participants")