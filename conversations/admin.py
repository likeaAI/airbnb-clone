from django.contrib import admin
from . import models


# Register your models here.


@admin.register(models.Messeage)
class MessageAdmon(admin.ModelAdmin) : 
    pass


@admin.register(models.Conversation)
class ConversationAdmoin(admin.ModelAdmin) : 
    pass