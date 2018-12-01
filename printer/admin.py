from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Product, ManufacturerInfo, User
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('sn','name',)
    search_fields = ('name','sn',)
    list_filter = ('name','sn',)


class ManufacturerInfoAdmin(admin.ModelAdmin):
    list_display = ('manufacturer','address',)
    search_fields = ('manufacturer',)


class UserAdmins(UserAdmin, admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('username', 'name', 'password', 'is_superuser','is_active','user_info')
        }),)

    list_display = ('username', 'user_info',)
    search_fields = ('username',)


admin.site.register(Product, ProductAdmin)
admin.site.register(ManufacturerInfo, ManufacturerInfoAdmin)
admin.site.register(User, UserAdmins)


