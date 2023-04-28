
"""class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','image','description')
    admin.site.register(Catagory,CategoryAdmin)
    """
from django.contrib import admin
from .models import *


admin.site.register(Catagory)
admin.site.register(Product)