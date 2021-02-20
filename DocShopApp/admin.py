from django.contrib import admin
from .models import DocShopApp

class DocShopAppAdmin (admin.ModelAdmin):
    list_display = ('username', 'email', 'country_code', 'phone_number', 'password')

admin.site.register(DocShopApp, DocShopAppAdmin)

