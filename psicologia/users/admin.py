from django.contrib import admin
from .models import *
from django.contrib import admin 



# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    model=CustomUser

    exclude = ['first_name', 'last_name', 'is_staff', 'is_superuser', 'groups', 'user_permissions']


    list_display =  [
            'email',
            'first_name',
            'last_name',
            'is_active',
            'date_joined'
        ]

class BuisnesUserAdmin(admin.ModelAdmin):
    model=BuisnesUser

    exclude = ['username','first_name', 'last_name', 'is_staff', 'is_superuser', 'groups', 'user_permissions']

    list_display =  [
            'email',
            'companie_name',
            'billing_address',
            'is_active',
            'payment_method'
        ]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(BuisnesUser, BuisnesUserAdmin)