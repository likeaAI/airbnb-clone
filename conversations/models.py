from tkinter import CASCADE
from django.db import models
from core import models as core_models
# Create your models here.


class Conversation(core_models.TimeStampedModel) : 

    participants = models.ManyToManyField("users.User" , blank=True) 

    def __str__(self) : 
        return str(self.creted)


class Messeage(core_models.TimeStampedModel) : 
    message = models.TextField()
    user = models.ForeignKey("users.User" , on_delete=CASCADE)
    conversation = models.ForeignKey("Conversation" , on_delete=CASCADE)

    def __str__(self) :
        return f"{self.user} says: {self.text}"

