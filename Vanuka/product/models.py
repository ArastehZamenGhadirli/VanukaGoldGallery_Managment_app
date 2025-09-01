from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.



class product(models.Model):
    name = models.CharField(max_length=20)
    weight = models.PositiveIntegerField()
    craftingfee_buy = models.PositiveBigIntegerField()
    craftingfee_sell = models.PositiveBigIntegerField()
    Is_available = models.BooleanField()
    bonakdaricode = models.CharField(max_length=30)
    bonakdariname = models.CharField(max_length=40)
    
    
    def __str__(self):
        return self.name
    
    
class Customer(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    phone_number = PhoneNumberField(unique=True, region="IR")
    
        
    def __str__(self):
        return f"{self.name} - {self.phone_number}"
    
    
    