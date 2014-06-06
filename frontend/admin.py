from django.contrib import admin
from frontend.models import ImportNote, Customer, CustomerContact, Size, Medium, \
    Supplier, Product, Catalog, CatalogIssue, CatalogIssueProduct, \
    RoyaltyGroup, PriceLevel, Order, OrderStatus, OrderProduct, Company, Invoice, Note


class OrderProductInline(admin.StackedInline):
    model = OrderProduct


class InvoiceInline(admin.StackedInline):
    model = Invoice

# Register your models here.
admin.site.register(ImportNote)
admin.site.register(Customer)
admin.site.register(CustomerContact)
admin.site.register(Size)
admin.site.register(Medium)
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Catalog)
admin.site.register(CatalogIssue)
admin.site.register(CatalogIssueProduct)
admin.site.register(RoyaltyGroup)


class PriceLevelAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'id', 'min_amount', 'max_amount', 'cost_per_item')

admin.site.register(PriceLevel, PriceLevelAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_date', 'pk', 'customer', 'total_cost', 'last_read')
    raw_id_fields = ('customer',)
    filter_horizontal = ('notes', 'products')
    inlines = [
        OrderProductInline, InvoiceInline
    ]

admin.site.register(Order, OrderAdmin)


class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('order', 'status', 'timestamp')
    raw_id_fields = ('order', )

admin.site.register(OrderStatus, OrderStatusAdmin)


class OrderProductAdmin(admin.ModelAdmin):
    raw_id_fields = ('order', 'product')

admin.site.register(OrderProduct, OrderProductAdmin)
admin.site.register(Company)


class InvoiceAdmin(admin.ModelAdmin):
    raw_id_fields = ('order',)
    list_display = ('order', 'company', 'number', 'timestamp')
    list_filter = ('company', 'timestamp')

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Note)