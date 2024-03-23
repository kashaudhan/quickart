from django.contrib import admin
from .models import Cart, CartItem


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'quantity', 'is_active')


admin.site.register(Cart)
admin.site.register(CartItem, CartItemAdmin)
