from django.db import models




class Category (models.Model):
    name = models.CharField(max_length=200, default="Party")
    description = models.CharField(max_length=1000, default="Party")

class Event(models.Model):
    name = models.CharField(max_length=200, default="Party")
    url = models.CharField(max_length=500, default="https://moi-portal.ru/upload/iblock/d9e/d9e5efcd756fe6681d27e921f9f2599a.jpg")
    description = models.CharField(max_length=1000, default="Party")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)





