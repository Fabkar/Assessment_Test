from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.permissions import IsAdminUser
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from backend.serializer import UserSerializer, OrderSerializer, ShippingSerializer, PaymentSerializer
from backend.models import Client, Order, Shipping, Payment
from rest_framework.authtoken.models import Token
import hashlib
from .models import ENV

class UserViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = UserSerializer

    @action(methods=['POST'], url_path='login', detail=False)
    def login(self, request):
        secret = ENV.get('SECRET')
        email = request.data.get('email')
        user = Client.objects.filter(email=email)
        password = request.data.get('password')
        if user is None:
            return Response({'Error': 'Not user found'}, status=204)
        self.password = hashlib.pbkdf2_hmac(
            'sha256', self.password.encode(), secret.encode(), 100000).hex()
        if password != user.get('password'):
            return Response({'Error': 'Invalid password'}, status=204)
        token = Token.objects.create(user)
        return Response({'token': token}, status=201)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(methods=['GET'], detail=False , url_path='shippings', url_name="Order_Shipping")
    def or_shipping(self, request):
        key, value = next(self.request.query_params.items())
        if key == 'country':
            shippings = Shipping.objects.filter(country=value)
        elif key == 'state':
            shippings = Shipping.objects.filter(state=value)
        else:
            shippings == Shipping.objects.filter(city=value)
        print(shippings)
        orders = []
        for shipping in shippings:
            orders.append(OrderSerializer(shipping.order).data)
        return Response({"orders": orders}, status=200)


    def get_queryset(self):
        id = self.request.query_params.get('gov_id')
        query = Order.objects.filter(client=id)
        return query

class ShippingViewSet(viewsets.ModelViewSet):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

def index(request):
    return HttpResponse("Hi everybody this is a company retailer")

# @api_view(["GET", "POST"])
# def list_user(request):
#     """List Costumer or create new Costumer"""
#     if request.method == "GET":
#         data = []
#         nextPage = 1
#         previousPage = 1
#         users = Client.objects.all()
#         page = request.GET.get('pages', 1)
#         paginator = Paginator(users, 10)
#         try:
#             data = paginator.page(page)
#         except PageNotAnInteger:
#             data = paginator.page(1)
#         except EmptyPage:
#             data = paginator.page(paginator.num_pages)

#         serializer = UserSerializer(data, context={"request":request}, many=True)
#         if data.has_next():
#             nextPage = data.next_page_number()
#         if data.has_previous():
#             previousPage = data.previous_page_number()
#         return Response({'data': serializer.data ,
#                          'count': paginator.count,
#                          'numpages' : paginator.num_pages,
#                          'nextlink': 'user/?page=' + str(nextPage),
#                          'prevlink': 'user/?page=' + str(previousPage)})

#     elif request.method == "POST":
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def client_detail(request, gov_id):
#     """Retrieve, update or delete a customer by gov_id/pk."""
#     try:
#         client = Client.objects.get(pk=gov_id)
#     except Client.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = UserSerializer(client,context={'request': request})
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = UserSerializer(client, data=request.data,context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         client.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(["GET", "POST"])
# def list_orders(request):
#     if request.method == "GET":
#         order = Order.objects.all()
#         serializer = OrderSerializer(order, context={"request":request}, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.create()
#             return Response(serializer.data)

