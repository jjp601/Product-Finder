from django.contrib import admin

from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date',)


admin.site.register(Product,ProductAdmin)
