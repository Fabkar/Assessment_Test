from django.db import models
from datetime import date

class Client(models.Model):
    """Define all fields about the costumer"""
    gov_id = models.CharField(max_length=30, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    company = models.CharField(max_length=30)
    password = models.CharField(max_length=50, null=False)

    def __str__(self):
        """Method that how to show the class costumer"""
        return f" {self.first_name} | {self.gov_id} "

class Order(models.Model):
    """Class Defines a purchase order to each costumer"""
    order_id = models.AutoField(primary_key=True)
    client = models.ForeignKey("Client", on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    taxes = models.FloatField()
    paid = models.BooleanField(null=True)

    def __str__(self):
        """Method Defines how to show the class Order"""
        return f" {str(self.client)} | {self.order_id} "


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
    order = models.OneToOneField("Order", on_delete=models.CASCADE)
    payment = models.OneToOneField("Payment", on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=4, choices=CITIES, default="MED")
    state = models.CharField(max_length=4, choices=STATES, default='ANT')
    country = models.CharField(max_length=4, choices=COUNTRIES, default='COL')
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        """Method Defines how to show the class shipping"""
        return f" {self.order} "

class Payment(models.Model):
    """Class Defines all atributes about payment"""
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
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
    date = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=4, choices=STATUS)

    def __str__(self):
        """Method Defines how to show the class payment"""
        return f" {self.order} | {self.type_payment} "
