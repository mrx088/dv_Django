from django.contrib import admin
from .models import Item,OrderItem,Order,Category

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin) :
    prepopulated_fields = {'slug':('title',)}

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin) :
    prepopulated_fields = {'slug':('name',)}




class InlineOrderItem(admin.TabularInline):
    model = OrderItem



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (InlineOrderItem,)

