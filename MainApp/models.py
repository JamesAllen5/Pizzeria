from django.db import models

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Toppings(models.Model):
    Pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    topping_name = models.TextField()
    
    def __str__(self):
        return f"{self.text[:50]}..."