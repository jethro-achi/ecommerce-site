from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('members/', views.members, name='members'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.indexpage, name='indexpage'),
    path('members/', views.members, name='members'),  # Add this line
    path('shopitem/', views.shopitempage, name='shopitempage'),  # Existing URL pattern for 'shopitempage'
    # Rest of the URL patterns
    
]
