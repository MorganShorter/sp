# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime
from django.conf import settings


class ImportNote(models.Model):
    """ Import notes
    """
    model = models.CharField(max_length=50)
    model_id = models.PositiveIntegerField()
    type = models.CharField(max_length=50, default=None)
    text = models.TextField()
    note = models.TextField(null=True, blank=True)
    src_model = models.CharField(max_length=50, null=True, blank=True)
    src_model_id_field = models.CharField(max_length=50, null=True, blank=True)
    src_model_id_text = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.type + ' Import Note for ' + self.model + '.id = ' + str(self.model_id)


class Customer(models.Model):
    """ Customer; makes an order from SmartPractice
    """
    registration = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    customer_type = models.CharField(max_length=255)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255)
    suburb = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=100, default='Australia')
    telephone = models.CharField(max_length=40)
    fax = models.CharField(max_length=40)
    email = models.EmailField(max_length=255)
    delivery_attn = models.CharField(max_length=255)
    delivery_address_line_1 = models.CharField(max_length=255)
    delivery_address_line_2 = models.CharField(max_length=255)
    delivery_suburb = models.CharField(max_length=100)
    delivery_state = models.CharField(max_length=100)
    delivery_postcode = models.CharField(max_length=10)
    delivery_country = models.CharField(max_length=100, default='Australia')
    from_src_company_id = models.IntegerField(null=True, blank=True)
    from_src_membadd_id = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=150)
    notes = models.ManyToManyField('Note', related_name='c_notes', blank=True)

    def save(self, *args, **kwargs):
        self.set_slug()
        super(Customer, self).save(*args, **kwargs)

    def set_slug(self):
        if not self.slug:
            self.slug = "%i-%s" % (Customer.objects.last().pk + 1, slugify(self.name))

    @property
    def same_delivery_address(self):
        if self.address_line_1 == self.delivery_address_line_1 and \
                self.address_line_2 == self.delivery_address_line_2 and \
                self.delivery_suburb == self.suburb and \
                self.delivery_state == self.state and \
                self.delivery_postcode == self.postcode and \
                self.name == self.delivery_attn:
            return True
        return False
 
    def __unicode__(self):
        return self.name


class CustomerContact(models.Model):
    """ Contact for a Customer
    """
    customer = models.ForeignKey(Customer, related_name='contacts')
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=40, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.surname)

    def info(self):
        ret = '%s %s' % (self.first_name, self.surname)
        if self.phone:
            ret = '%s, %s' % (ret, self.phone)
        if self.email:
            ret = '%s, %s' % (ret, self.email)

        return ret


class Size(models.Model):
    """ Product Size/Dimensions
    """
    width = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    depth = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    units = models.CharField(max_length=80, null=True)
    notes = models.TextField(null=True)
    sub_notes = models.TextField(null=True)

    class Meta:
        ordering = ('width', 'height', 'depth', 'units')

    def __unicode__(self):
        if self.width and self.height and self.depth:
            return "W:%d H:%d D:%d" % (self.width, self.height, self.depth)
        elif self.width and self.height:
            return "W:%d H:%d" % (self.width, self.height)
        else:
            return self.notes


class Medium(models.Model):
    """ Product Medium
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    notes = models.TextField(null=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.description


class RoyaltyImg(models.Model):
    """ Royalty Percent/Img for a Product
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    image = models.ImageField(upload_to='royalty_images', max_length=255, height_field='image_height', width_field='image_width', null=True)
    image_height = models.PositiveSmallIntegerField(null=True)
    image_width = models.PositiveSmallIntegerField(null=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __unicode__(self):
        return self.name


class Supplier(models.Model):
    """ Supplier of Products SP sells (SP, JH, AIO, ...)
    """
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=150)

    class Meta:
        ordering = ('code', 'name')

    def __unicode__(self):
        return "%s : %s" % (self.code, self.name)


class Product(models.Model):
    """ Products SmartPractice sells; supplied by Suppliers
    """
    code = models.CharField(max_length=60)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    notes = models.ManyToManyField('Note', related_name='p_notes', blank=True)
    message = models.TextField()
    current_stock = models.PositiveIntegerField(default=0)
    minimum_stock = models.PositiveIntegerField(default=0)
    sp_cost = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    size = models.ForeignKey(Size, related_name='+', on_delete=models.PROTECT)
    medium = models.ForeignKey(Medium, related_name='+', null=True, on_delete=models.PROTECT)
    royalty_img = models.ForeignKey(RoyaltyImg, related_name='+', null=True, on_delete=models.PROTECT)
    supplier = models.ForeignKey(Supplier, related_name='products', on_delete=models.PROTECT)
    royalty = models.PositiveSmallIntegerField(help_text='[0..100]%', default=0)
    last_read = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.code)

    @property
    def unit_cost(self):
        return float(float(self.sp_cost) * (1.00 + float(self.royalty) / 100))


class Catalog(models.Model):
    """ Catalog's SmartPractice advertise products in
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=150)

    def save(self, *args, **kwargs):
        super(Catalog, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = "%i-%s" % (self.id, slugify(self.name))
            super(Catalog, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class CatalogIssue(models.Model):
    """ An Issue of a Catalog
    """
    catalog = models.ForeignKey(Catalog, related_name='issues')
    products = models.ManyToManyField(Product, related_name='catalog_issues', through='CatalogIssueProduct')
    issue = models.CharField(max_length=80)
    slug = models.SlugField(unique=True, max_length=150)

    def save(self, *args, **kwargs):
        super(CatalogIssue, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = "%i-%s" % (self.id, slugify("%s-%s" % (self.catalog.name, self.issue)))
            super(CatalogIssue, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.issue


class CatalogIssueProduct(models.Model):
    """ Product advertised in specific issue of a catalog
    """
    page_ref = models.PositiveSmallIntegerField()
    img_ref = models.PositiveSmallIntegerField()
    sub_ref = models.CharField(max_length=3, null=True, blank=True)
    catalog_issue = models.ForeignKey(CatalogIssue)
    product = models.ForeignKey(Product)
    slug = models.SlugField(unique=True, max_length=150)

    def save(self, *args, **kwargs):
        super(CatalogIssueProduct, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = "%i-%s" % (self.id, slugify("%s-%s-%s" % (self.catalog_issue.catalog.name, self.catalog_issue.issue, self.product.name)))
            super(CatalogIssueProduct, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s features in Issue %s of Catalog %s on Page %s Reference %s, %s" % (self.product, self.catalog_issue, self.catalog_issue.catalog, self.page_ref, self.img_ref, self.sub_ref)


class PriceLevelGroup(models.Model):
    """ Price Level Group for a PriceLevel; 'AR', 'LI', etc..
    """
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=255, null=True, blank=True)
    royalty = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class PriceLevel(models.Model):
    """ Price Level for a Product; products can have multiple price levels
    """
    product = models.ForeignKey(Product, related_name='price_levels', null=True, blank=True)
    min_amount = models.PositiveIntegerField()
    max_amount = models.PositiveIntegerField(blank=True, null=True)
    cost_per_item = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    cost_per_block = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    block_only = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return 'Level #%s' % self.pk

    class Meta:
        ordering = ('-min_amount',)


class Order(models.Model):
    """ Order placed by a Customer for Product(s) sold by SmartPractice
    """
    customer = models.ForeignKey(Customer, related_name='orders')
    products = models.ManyToManyField(Product, related_name='+', through='OrderProduct')
    sub_total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    shipping_cost = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    tax = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    sp_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    order_date = models.DateTimeField(default=datetime.now)
    wanted_by = models.DateTimeField(default=datetime.now)

    invoice_company_name = models.CharField(max_length=255)
    invoice_company_reg = models.CharField(max_length=120)
    invoice_address_line_1 = models.CharField(max_length=255)
    invoice_address_line_2 = models.CharField(max_length=255)
    invoice_suburb = models.CharField(max_length=100)
    invoice_state = models.CharField(max_length=100)
    invoice_postcode = models.CharField(max_length=10)
    invoice_country = models.CharField(max_length=100)

    shipping_attn = models.CharField(max_length=255)
    shipping_address_line_1 = models.CharField(max_length=255)
    shipping_address_line_2 = models.CharField(max_length=255)
    shipping_suburb = models.CharField(max_length=100)
    shipping_state = models.CharField(max_length=100)
    shipping_postcode = models.CharField(max_length=10)
    shipping_country = models.CharField(max_length=100)

    from_src_order_id = models.IntegerField(null=True, blank=True)
    from_borders_fakeid = models.IntegerField(null=True, blank=True)

    order_notes = models.CharField(max_length=510, null=True, blank=True)
    notes = models.ManyToManyField('Note', related_name='o_notes')

    @property
    def order_date_str(self):
        return '%s' % self.order_date.strftime("%Y-%m-%d")

    @property
    def order_month_str(self):
        return '%s' % self.order_date.strftime("%Y-%m")

    @property
    def last_invoice(self):
        return self.invoices.order_by('-timestamp')[0] if self.invoices.count() else None

    @property
    def last_status(self):
        return self.statuses.order_by('-timestamp')[0] if self.statuses.count() else None

    def __unicode__(self):
        return 'Order %s' % self.pk

    def total_recount(self, save=False):
        self.sub_total = 0
        self.discount = 0
        self.total_cost = 0
        self.sp_cost = 0
        self.tax = 0

        for order_product in self.ordered_products.all():
            self.sub_total += order_product.total_cost
            self.tax += order_product.total_tax
            self.discount += order_product.discount_price * order_product.quantity
            self.sp_cost += order_product.sp_price * order_product.quantity

        self.total_cost = self.sub_total + float(self.shipping_cost) - float(self.discount)

        if save:
            self.save(total_recount=False)

    def save(self, total_recount=True, *args, **kwargs):
        if total_recount:
            self.total_recount(save=False)
        super(Order, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-order_date',)


class OrderStatus(models.Model):
    """ Status for an Order; an Order can have multiple OrderStatus's as it progresses from Processing -> Shipped etc
    """
    PROCESSING = 'PS'
    CONFIRMED = 'CF'
    AWAITING_PAYMENT = 'AP'
    AWAITING_STOCK = 'AS'
    CANCELLED = 'CN'
    IN_FORFILLMENT = 'IF'
    SHIPPED = 'SD'
    ORDER_STATUS_CHOICES = (
        (PROCESSING, 'Processing'),
        (CONFIRMED, 'Confirmed'),
        (AWAITING_PAYMENT, 'Awaiting Payment'),
        (AWAITING_STOCK, 'Awaiting Stock (Back Order)'),
        (CANCELLED, 'Cancelled'),
        (IN_FORFILLMENT, 'In Forfillment'),
        (SHIPPED, 'Complete (Shipped)'),
    )
    STATUSES = [x[0] for x in ORDER_STATUS_CHOICES]

    order = models.ForeignKey(Order, related_name='statuses')
    status = models.CharField(max_length=2, choices=ORDER_STATUS_CHOICES, default=PROCESSING)
    notes = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)

    def __unicode__(self):
        return '%s - %s' % (self.order, self.status)

    class Meta:
        ordering = ('-timestamp',)


class OrderProduct(models.Model):
    """ 'Line Item' for an order; contains Product ordered on an Order with its quantity
    """
    order = models.ForeignKey(Order, related_name='ordered_products')
    product = models.ForeignKey(Product)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    unit_tax = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    discount_price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    sp_price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    royalty_amount = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    back_order = models.BooleanField(default=False)
    with_tax = models.BooleanField(default=False)

    class Meta:
        ordering = ('product__code',)

    def __unicode__(self):
        return '%s %s' % (self.order, self.product)

    def save(self, *args, **kwargs):
        print 'order_product save'
        self.sp_price = self.product.sp_cost
        self.unit_tax = 0 if not self.with_tax else float(self.unit_price * settings.TAX_PERCENT) / 100
        self.discount_price = self.unit_price * self.discount_percentage / 100
        self.royalty_amount = self.quantity * (float(self.unit_price) - float(self.sp_price))
        self.back_order = True if self.quantity > self.product.current_stock else False
        super(OrderProduct, self).save(*args, **kwargs)

    @property
    def total_cost(self):
        if self.with_tax:
            return float(self.unit_price) * self.quantity * (float(settings.TAX_PERCENT) / 100 + 1)
        return float(self.unit_price * self.quantity)

    @property
    def total_tax(self):
        if self.with_tax:
            return float(self.unit_price) * self.quantity * float(settings.TAX_PERCENT) / 100
        return 0


class Company(models.Model):
    """ The various companies SmartPractice trade as; 'CAA' 'SP' etc
    """
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    fax = models.CharField(max_length=25)
    registration = models.CharField(max_length=100)
    logo_img = models.ImageField(upload_to='company_logos', max_length=255, height_field='logo_height', width_field='logo_width', null=True)
    logo_height = models.PositiveSmallIntegerField(null=True)
    logo_width = models.PositiveSmallIntegerField(null=True)

    def __unicode__(self):
        return self.name


class Invoice(models.Model):
    """ An Invoice for an Order issued by a particular Company that SmartPractices trades as
    """
    order = models.ForeignKey(Order, related_name='invoices')
    company = models.ForeignKey(Company, related_name='+')
    number = models.PositiveIntegerField()
    timestamp = models.DateTimeField(default=datetime.now, auto_now_add=True)

    def __unicode__(self):
        return 'Order %s; Number: %s' % (self.order, self.number)


class Note(models.Model):
    text = models.TextField()
    create_dt = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s...' % self.text[:30]