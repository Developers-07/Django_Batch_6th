from django.contrib import admin
from .models import Customer

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):

    search_fields = ['name', 'email']
    list_filter = ['name', 'phone']
    list_display = ['name', 'email', 'phone']
    list_per_page = 10

admin.site.register(Customer, CustomerAdmin)


