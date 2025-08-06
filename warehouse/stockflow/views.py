from django.shortcuts import render, redirect
from .forms import ProductForm, StockTransactionForm, StockEntryForm
from .models import Product, StockTransaction, StockEntry
from django.db.models import Sum, Case, When, IntegerField

def home(request):
    return render(request, 'home.html')

def add_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'add_products.html', {'form': form})

def add_transaction(request):
    if request.method == 'POST':
        transaction_form = StockTransactionForm(request.POST)
        entry_form = StockEntryForm(request.POST)
        if transaction_form.is_valid() and entry_form.is_valid():
            transaction = transaction_form.save()
            entry = entry_form.save(commit=False)
            entry.transaction = transaction
            entry.save()
            return redirect('home')
    else:
        transaction_form = StockTransactionForm()
        entry_form = StockEntryForm()
    return render(request, 'add_transaction.html', {
        'transaction_form': transaction_form,
        'entry_form': entry_form
    })

def inventory_report(request):
    inventory = Product.objects.all().annotate(
        stock_in=Sum(Case(When(stockentry__transaction__transaction_type='IN', then='stockentry__quantity'),
                          output_field=IntegerField())),
        stock_out=Sum(Case(When(stockentry__transaction__transaction_type='OUT', then='stockentry__quantity'),
                           output_field=IntegerField()))
    )
    for product in inventory:
        product.balance = (product.stock_in or 0) - (product.stock_out or 0)
    return render(request, 'inventory.html', {'inventory': inventory})