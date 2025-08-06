from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the product")
    sku = models.CharField(max_length=50, unique=True, help_text="Unique Stock Keeping Unit (SKU)")
    description = models.TextField(blank=True, help_text="Optional description of the product")

    def __str__(self):
        return f"{self.name} ({self.sku})"


class StockTransaction(models.Model):
    TRANSACTION_TYPES = [
        ('IN', 'Stock In'),
        ('OUT', 'Stock Out'),
    ]

    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPES)
    reference_note = models.CharField(max_length=255, blank=True, help_text="Optional reference or reason for transaction")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_transaction_type_display()} on {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


class StockEntry(models.Model):
    transaction = models.ForeignKey(StockTransaction, on_delete=models.CASCADE, related_name='entries')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(help_text="Quantity affected by this transaction")

    class Meta:
        unique_together = ('transaction', 'product')  # One product per transaction

    def __str__(self):
        return f"{self.product.name} - {self.quantity} units ({self.transaction.transaction_type})"
