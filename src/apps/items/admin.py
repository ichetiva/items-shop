from django.contrib import admin

from .models import Item, ItemPrice


class ItemAdmin(admin.ModelAdmin):
    pass


class ItemPriceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemPrice, ItemPriceAdmin)
