from django.contrib import admin
from frontend.models import ImportNote, Customer, CustomerContact, Size, Medium, RoyaltyImg, Supplier, Product, Catalog, CatalogIssue, CatalogIssueProduct, PriceLevelGroup, PriceLevel, Order, OrderStatus, OrderProduct, Company, Invoice

# Register your models here.
admin.site.register(ImportNote)
admin.site.register(Customer)
admin.site.register(CustomerContact)
admin.site.register(Size)
admin.site.register(Medium)
admin.site.register(RoyaltyImg)
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Catalog)
admin.site.register(CatalogIssue)
admin.site.register(CatalogIssueProduct)
admin.site.register(PriceLevelGroup)
admin.site.register(PriceLevel)
admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(OrderProduct)
admin.site.register(Company)
admin.site.register(Invoice)
