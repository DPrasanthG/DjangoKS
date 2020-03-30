from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=50, null=True)
    customer_contact = models.CharField(max_length=50, null=True)
    customer_addr = models.CharField(max_length=300, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.customer_name

class Product(models.Model):
    product_name = models.