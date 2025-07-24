from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.product import ProductPriceHistory
from .models.waste import Waste
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Products,AdminProduct)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(ProductPriceHistory)
from django.contrib import admin
from store.models.waste import Waste

class WasteAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'waste_category', 'total_kg', 'status', 'image_preview')
    list_filter = ('waste_category', 'status')
    search_fields = ('name', 'mobile', 'waste_category')

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="50" height="50" style="border-radius: 5px;">'
        return "No Image"
    
    image_preview.allow_tags = True
    image_preview.short_description = "Image Preview"

admin.site.register(Waste, WasteAdmin)



# username = Tanushree, email = tanushree7252@gmail.com, password = 1234
