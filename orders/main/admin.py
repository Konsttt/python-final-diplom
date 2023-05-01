from django.contrib import admin
from .models import Shop, Contact, Category, Product, ProductInfo, Parameter, \
    ProductParameter, Order, OrderItem, ConfirmEmailToken, User, UserManager


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'password', 'email']


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url', 'user', 'state']






admin.register()
