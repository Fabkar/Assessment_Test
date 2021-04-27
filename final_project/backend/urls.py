from django.urls import path
from backend import views

urlpatterns = [
    path('', views.list_user, name="users"),
    path('<gov_id>/', views.client_detail, name="detail users"),
]
