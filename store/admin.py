from django.contrib import admin
from .models import Product
from .models import Order, OrderItem
from .models import Category, Product
from .models import ContactMessage

admin.site.register(Product)
admin.site.register(Category)

admin.site.register(Order)
admin.site.register(OrderItem)





@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    search_fields = ('name', 'email', 'message')
    ordering = ('-created_at',)
