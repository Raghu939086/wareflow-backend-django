from django.contrib import admin
from .models import Product, StockTransaction, StockEntry

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'description')
    search_fields = ('name', 'sku')

@admin.register(StockTransaction)
class StockTransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_type', 'reference_note', 'timestamp')
    list_filter = ('transaction_type', 'timestamp')

@admin.register(StockEntry)
class StockEntryAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'product', 'quantity')
    search_fields = ('product__name',)