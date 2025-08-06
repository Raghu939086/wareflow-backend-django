from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-product/', views.add_product, name='add_product'),
    path('add-transaction/', views.add_transaction, name='add_transaction'),
    path('inventory/', views.inventory_report, name='inventory'),
]