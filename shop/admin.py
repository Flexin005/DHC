from django.contrib import admin
from .models import Category, Product, Order, OrderItem, ad, bestoffer
from django.contrib.auth.models import User, Group

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20
    search_fields = ['name', 'description']


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock',
                    'available', 'created', 'updated', 'best_seller']
    list_editable = ['price', 'stock', 'available', 'best_seller']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20
    search_fields = ['name', 'description']


admin.site.register(Product, ProductAdmin)


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    fieldsets = [
        ('Product', {'fields': ['product'], }),
        ('Quantity', {'fields': ['quantity'], }),
        ('Price', {'fields': ['price'], }),
    ]
    readonly_fields = ['product', 'quantity', 'price']
    can_delete = False
    max_num = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'billingName', 'emailAddress', 'created']
    list_display_links = ('id', 'billingName', 'emailAddress')
    search_fields = ['id', 'billingName', 'emailAddress']
    readonly_fields = ['id', 'token', 'total', 'emailAddress', 'created', 'billingName', 'billingAddress1', 'billingCity',
                       'billingPostcode', 'billingCountry', 'shippingName', 'shippingAddress1', 'shippingCity', 'shippingPostcode', 'shippingCountry']

    field_sets = [
        ('ORDER INFORMATION', {'fields': [
         'id', 'token', 'total', 'created']}),
        ('BILLING INFORMATION', {'fields': ['billingName', 'billingAddress1', 'billingCity',
                                            'billingPostcode', 'billingCountry', 'emailAddress']}),
        ('SHIPPING INFORMATION', {'fields': ['shippingName', 'shippingAddress1', 'shippingCity',
                                             'shippingPostcode', 'shippingCountry']}),
    ]

    inlines = [
        OrderItemAdmin,
    ]

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return False

class adAdmin(admin.ModelAdmin):
    list_display = ['name', 'created']
admin.site.register(ad, adAdmin)

class bestofferAdmin(admin.ModelAdmin):
    list_max_items = 1
admin.site.register(bestoffer)

