# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 15:06:59 2020

@author: az
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]