from django import forms
from .models import Product, StockTransaction, StockEntry

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sku', 'description']

class StockTransactionForm(forms.ModelForm):
    class Meta:
        model = StockTransaction
        fields = ['transaction_type', 'reference_note']

class StockEntryForm(forms.ModelForm):
    class Meta:
        model = StockEntry
        fields = ['product', 'quantity']