from django.contrib import admin
from .models import Product,ProductsImages,Brand,Category,ProductReview

class ProductImageTabular(admin.TabularInline):
    model = ProductsImages
    

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageTabular]
    list_display = ['name', 'flag' ,'quantity','price']
    list_filter = ['flag','brand','category' ]
    search_fields = ['name', 'desc','subtitle']


admin.site.register(Product,ProductAdmin)
admin.site.register(ProductsImages)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(ProductReview)
