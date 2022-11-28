from django.contrib import admin
from apps.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_categories', 'language', 'year']
    list_filter = ['category', 'language', 'year', 'created_date', 'last_update']
    # exclude = ["size", "size_type", "file_type", "rate", "created_date", "last_update"]
    list_display_links = ['name', ]
    search_fields = ['name', 'category']
    ordering = ['-id']

    def get_categories(self, obj):
        return ' | '.join([c.name for c in obj.category.all().only('name')])

