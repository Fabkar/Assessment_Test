from rest_framework import serializers
from backend.models import Client, Order

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
