from django.db import models

# Create your models here.
class Registration(models.Model):
    co_operativename = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.address

class Production(models.Model):
    cooperative_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    date = models.DateField(max_length=255)
   
    
    def _str_(self):
        return self.address 

class Product(models.Model):
    fish_name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    date = models.DateField(max_length=255)
   
    
    def _str_(self):
        return self.quantity 