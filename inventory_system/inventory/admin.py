from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):  # class name changed to match Product
    list_display = ('name', 'price', 'quantity')  # Adjust as needed

# Optional customization for admin panel display
admin.site.site_header = "Inventory Control Management"
admin.site.site_title = "Inventory Control Management"
admin.site.index_title = "Welcome to Inventory Dashboard"