from django.urls import path
from . import views
from .views import identify_contact

urlpatterns = [
    path('',views.index,name='index'),
   
    path('identify/', views.identify_contact, name='identify_contact'),
]
