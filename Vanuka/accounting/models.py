from django.db import models
from product.models import Customer,product
# Create your models here.


class Invoice(models.Model):
    date_of_sell = models.DateField()
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE , related_name="Customer_Invoice")
    product = models.OneToOneField(product , on_delete=models.PROTECT , related_name="Product_Invoice")




