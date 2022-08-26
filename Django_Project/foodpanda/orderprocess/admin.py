from django.contrib import admin
from .models import FuturegfList

# Register your models here.

class MakeBeautiful(admin.ModelAdmin):
    search_fields = ['Name']
    list_display = ['Name', 'Phone', 'Email', 'Age']
    list_filter = ['Name', 'Phone', 'Email', 'Address', 'Age']


admin.site.register(FuturegfList, MakeBeautiful)