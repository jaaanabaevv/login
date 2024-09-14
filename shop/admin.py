from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Comment)



@admin.register(Product)
class ProductClass(admin.ModelAdmin):
    list_display = ['name','price','stock','category','show_image']
    list_display_links = ['name','stock','category']
    list_filter = ['category']
    list_editable = ['price']

    def show_image(self,photo):
        if photo.image:
            return mark_safe(f"<img src='{photo.image.url}' width=100>")
        return None
    show_image.__name__='suwret'