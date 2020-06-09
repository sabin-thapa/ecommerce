from django.contrib import admin
from store.models import Customer, Order, OrderItem, Product, ShippingAddress

from import_export.admin import ImportExportModelAdmin
@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product)
admin.site.register(ShippingAddress)