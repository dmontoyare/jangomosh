from django.db import models

# se crea cada tabla como una clase, la cual tiene como padre models.Model
class Product(models.Model):
    # cada atributo es = a model. tipo de variable y sus argumentos (googlear django field types)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6 ,decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(error_messages=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
