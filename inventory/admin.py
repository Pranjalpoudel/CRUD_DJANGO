from django.contrib import admin
from .models import Category, Item

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'created_at')
    search_fields = ('name',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'status', 'price', 'updated_at')
    list_filter = ('category', 'status', 'created_at')
    search_fields = ('name', 'serial_number', 'description')
    date_hierarchy = 'created_at'
