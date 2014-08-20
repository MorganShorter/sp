from django.contrib import admin
from django import forms
from frontend.models import ImportNote, Customer, CustomerContact, Size, Medium, \
    Supplier, Product, Catalog, CatalogIssue, CatalogIssueProduct, \
    RoyaltyGroup, PriceLevel, Order, OrderStatus, OrderProduct, \
    Company, Invoice, Note, BackOrder, StockAdjust, SPUser, Document
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class OrderProductInline(admin.StackedInline):
    model = OrderProduct


class InvoiceInline(admin.StackedInline):
    model = Invoice

# Register your models here.
admin.site.register(ImportNote)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'customer_type', 'telephone', 'email')
    search_fields = ('name', 'from_src_company_id')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerContact)
admin.site.register(Size)
admin.site.register(Medium)
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Catalog)
admin.site.register(CatalogIssue)
admin.site.register(CatalogIssueProduct)
admin.site.register(RoyaltyGroup)


class BackOrderAdmin(admin.ModelAdmin):
    raw_id_fields = ('order_product',)
    list_display = ('timestamp', 'order_product', 'amount', 'complete')
    list_filter = ('complete',)

admin.site.register(BackOrder, BackOrderAdmin)


class StockAdjustAdmin(admin.ModelAdmin):
    raw_id_fields = ('product', 'user')
    list_display = ('timestamp', 'product', 'user')

admin.site.register(StockAdjust, StockAdjustAdmin)


class PriceLevelAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'id', 'min_amount', 'max_amount', 'cost_per_item')

admin.site.register(PriceLevel, PriceLevelAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_date', 'pk', 'customer', 'total_cost', 'last_read')
    raw_id_fields = ('customer',)
    filter_horizontal = ('notes', 'products')
    search_fields = ('from_src_order_id', 'id', 'customer__name')
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


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = SPUser
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = SPUser
        fields = ('email', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class SPUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('User Enhancements', {'fields': (
            'font_size',
            'font_weight',
            'bg_color',
            'label_bg_color',
            'font_color',
            'jodabrian_visible'
        )}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(SPUser, SPUserAdmin)
admin.site.unregister(Group)

admin.site.register(Document)