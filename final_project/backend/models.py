from django.db import models

class Client(models.Model):
    """Define all specifition about the costumer"""
    gov_id = models.CharField(max_length=30, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    company = models.CharField(max_length=30)

def __str__(self):
    """Method that how to show the class costumer"""
    return self.gov_id

class Order(models.Model):
    """Class Defines a purchase order to each costumer"""
    order_id = models.IntegerField(primary_key=True)
    gov_id = models.ForeignKey("Client", on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    taxes = models.DecimalField(max_digits=3, decimal_places=2)
    paid = models.BooleanField(null=True)

def __str__(self):
    """Method Defines how to show the class Order"""
    return self.order_id


class Shipping(models.Model):
    """Class that defines Specs about details shipping"""
    CITIES = (
        ('BOG', 'BOGOTA'),
        ('BARR', 'BARRANQUILLA'),
        ('CART', 'CARTAGENA'),
        ('CAL', 'CALI'),
        ('MED', 'MEDELLIN'),
    )
    STATES = (
        ('ANT', 'ANTIOQUIA'),
        ('ATL', 'ATLANTICO'),
        ('BOL', 'BOLIVAR'),
        ('CUND', 'CUNDINAMARCA'),
        ('VAC', 'VALLE DEL CAUCA'),
    )
    COUNTRIES = (
        ('COL', 'COLOMBIA'),
    )
    order_id = models.OneToOneField("Order", on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=4, choices=CITIES, default="MED")
    state = models.CharField(max_length=4, choices=STATES, default='ANT')
    country = models.CharField(max_length=4, choices=COUNTRIES, default='COL')
    cost = models.DecimalField(max_digits=10, decimal_places=2)

def __str__(self):
    """Method Defines how to show the class shipping"""
    return self.address


class Payment(models.Model):
    """Class Defines all atributes about payment"""
    order_id = models.ForeignKey("Order", on_delete=models.CASCADE)
    TYPE_PAYMENT = (
        ('CCARD', 'CREDIT CARD'),
        ('DEBIT', 'PSE'),
    )
    STATUS = (
        ('APR', 'APROBADO'),
        ('CANC', 'CANCELADA'),
        ('RECH', 'RECHAZADO'),
    )
    type_payment = models.CharField(max_length=5, choices=TYPE_PAYMENT, default="CCARD")
    date = models.DateField(auto_now=False, auto_now_add=False)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=4, choices=STATUS)

def __str__(self):
    """Method Defines how to show the class payment"""
    return self.type_payment

