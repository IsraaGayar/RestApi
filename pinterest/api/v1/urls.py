from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

from . import views

import pinterest

urlpatterns = [
    path('pins', views.PinList.as_view(),name='pinlist'),
    path('create', views.PinCreate.as_view(), name='pincreate'),
    path('pins/<int:pk>', views.PinDetail.as_view(),name='pindetails'),
    # path('login', obtain_auth_token),


    path('users', views.UserList.as_view(),name='userlist'),
    path('users/<int:pk>', views.UserDetail.as_view(),name='userdetails'),

]
