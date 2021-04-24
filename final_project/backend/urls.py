from django.urls import path

from backend import views
from django.conf.urls import url

urlpatterns = [
    # path('', views.index, name='index'),
    path('users/', views.list_user),
]
