from rest_framework import serializers
from backend.models import Client, Order, Payment, Shipping

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ['password']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = "__all__"

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
