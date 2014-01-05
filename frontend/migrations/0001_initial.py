# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ImportNote'
        db.create_table('frontend_importnote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('model_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('type', self.gf('django.db.models.fields.CharField')(default=None, max_length=50)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('note', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('src_model', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('src_model_id_field', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('src_model_id_text', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=150)),
        ))
        db.send_create_signal('frontend', ['ImportNote'])

        # Adding model 'Customer'
        db.create_table('frontend_customer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('registration', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('customer_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address_line_1', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address_line_2', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('suburb', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('country', self.gf('django.db.models.fields.CharField')(default='Australia', max_length=100)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('delivery_attn', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('delivery_address_line_1', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('delivery_address_line_2', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('delivery_suburb', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('delivery_state', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('delivery_postcode', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('delivery_country', self.gf('django.db.models.fields.CharField')(default='Australia', max_length=100)),
            ('from_src_company_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('from_src_membadd_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=150)),
        ))
        db.send_create_signal('frontend', ['Customer'])

        # Adding model 'CustomerContact'
        db.create_table('frontend_customercontact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='contacts', to=orm['frontend.Customer'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=150)),
        ))
        db.send_create_signal('frontend', ['CustomerContact'])

        # Adding model 'Size'
        db.create_table('frontend_size', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('width', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=4)),
            ('height', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=4)),
            ('depth', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=4)),
            ('units', self.gf('django.db.models.fields.CharField')(max_length=80, null=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True)),
            ('sub_notes', self.gf('django.db.models.fields.TextField')(null=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=150)),
        ))
        db.send_create_signal('frontend', ['Size'])

        # Adding model 'Medium'
        db.create_table('frontend_medium', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=150)),
        ))
        db.send_create_signal('frontend', ['Medium'])

        # Adding model 'RoyaltyImg'
        db.create_table('frontend_royaltyimg', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=255, null=True)),
            ('image_height', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('image_width', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('percentage', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=150)),
        ))
        db.send_create_signal('frontend', ['RoyaltyImg'])

        # Adding model 'Supplier'
        db.create_table('frontend_supplier', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=150)),
        ))
        db.send_create_signal('frontend', ['Supplier'])

        # Adding model 'Product'
        db.create_table('frontend_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('notes', self.gf('django.db.models.fields.TextField')()),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('current_stock', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('minimum_stock', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('sp_cost', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=2)),
            ('size', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['frontend.Size'])),
            ('medium', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['frontend.Medium'])),
            ('royalty_img', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['frontend.RoyaltyImg'])),
            ('supplier', self.gf('django.db.models.fields.related.ForeignKey')(related_name='products', to=orm['frontend.Supplier'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=150)),
        ))
        db.send_create_signal('frontend', ['Product'])

        # Adding model 'Catalog'
        db.create_table('frontend_catalog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=150)),
        ))
        db.send_create_signal('frontend', ['Catalog'])

        # Adding model 'CatalogIssue'
        db.create_table('frontend_catalogissue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('catalog', self.gf('django.db.models.fields.related.ForeignKey')(related_name='issues', to=orm['frontend.Catalog'])),
            ('issue', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=150)),
        ))
        db.send_create_signal('frontend', ['CatalogIssue'])

        # Adding model 'CatalogIssueProduct'
        db.create_table('frontend_catalogissueproduct', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page_ref', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('img_ref', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('sub_ref', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('catalog_issue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.CatalogIssue'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Product'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=150)),
        ))
        db.send_create_signal('frontend', ['CatalogIssueProduct'])

        # Adding model 'PriceLevelGroup'
        db.create_table('frontend_pricelevelgroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=150)),
        ))
        db.send_create_signal('frontend', ['PriceLevelGroup'])

        # Adding model 'PriceLevel'
        db.create_table('frontend_pricelevel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('price_level_group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='price_levels', null=True, to=orm['frontend.PriceLevelGroup'])),
            ('min_amount', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('max_amount', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('cost_per_item', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=2, blank=True)),
            ('cost_per_block', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=2, blank=True)),
            ('block_only', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=150)),
        ))
        db.send_create_signal('frontend', ['PriceLevel'])

        # Adding M2M table for field products on 'PriceLevel'
        db.create_table('frontend_pricelevel_products', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pricelevel', models.ForeignKey(orm['frontend.pricelevel'], null=False)),
            ('product', models.ForeignKey(orm['frontend.product'], null=False))
        ))
        db.create_unique('frontend_pricelevel_products', ['pricelevel_id', 'product_id'])

        # Adding model 'Order'
        db.create_table('frontend_order', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='orders', to=orm['frontend.Customer'])),
            ('sub_total', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=12, decimal_places=2)),
            ('shipping_cost', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=9, decimal_places=2)),
            ('tax', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=12, decimal_places=2)),
            ('discount', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=12, decimal_places=2)),
            ('total_cost', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=12, decimal_places=2)),
            ('sp_cost', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=12, decimal_places=2)),
            ('order_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('wanted_by', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('invoice_company_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('invoice_company_reg', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('invoice_address_line_1', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('invoice_address_line_2', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('invoice_suburb', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('invoice_state', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('invoice_postcode', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('invoice_country', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('shipping_attn', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('shipping_address_line_1', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('shipping_address_line_2', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('shipping_suburb', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('shipping_state', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('shipping_postcode', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('shipping_country', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('from_src_order_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('from_borders_fakeid', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('order_notes', self.gf('django.db.models.fields.CharField')(max_length=510, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=150)),
        ))
        db.send_create_signal('frontend', ['Order'])

        # Adding model 'OrderStatus'
        db.create_table('frontend_orderstatus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(related_name='statuses', to=orm['frontend.Order'])),
            ('status', self.gf('django.db.models.fields.CharField')(default='PS', max_length=2)),
            ('notes', self.gf('django.db.models.fields.TextField')()),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=150)),
        ))
        db.send_create_signal('frontend', ['OrderStatus'])

        # Adding model 'OrderProduct'
        db.create_table('frontend_orderproduct', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Order'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Product'])),
            ('quantity', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('unit_price', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=9, decimal_places=2)),
            ('unit_tax', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=9, decimal_places=2)),
            ('discount_percentage', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=5, decimal_places=2)),
            ('discount_price', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=9, decimal_places=2)),
            ('sp_price', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=9, decimal_places=2)),
            ('royalty_amount', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=9, decimal_places=2)),
            ('back_order', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=150)),
        ))
        db.send_create_signal('frontend', ['OrderProduct'])

        # Adding model 'Company'
        db.create_table('frontend_company', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('registration', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('logo_img', self.gf('django.db.models.fields.files.ImageField')(max_length=255, null=True)),
            ('logo_height', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('logo_width', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=150)),
        ))
        db.send_create_signal('frontend', ['Company'])

        # Adding model 'Invoice'
        db.create_table('frontend_invoice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(related_name='invoices', to=orm['frontend.Order'])),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['frontend.Company'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=150)),
        ))
        db.send_create_signal('frontend', ['Invoice'])


    def backwards(self, orm):
        # Deleting model 'ImportNote'
        db.delete_table('frontend_importnote')

        # Deleting model 'Customer'
        db.delete_table('frontend_customer')

        # Deleting model 'CustomerContact'
        db.delete_table('frontend_customercontact')

        # Deleting model 'Size'
        db.delete_table('frontend_size')

        # Deleting model 'Medium'
        db.delete_table('frontend_medium')

        # Deleting model 'RoyaltyImg'
        db.delete_table('frontend_royaltyimg')

        # Deleting model 'Supplier'
        db.delete_table('frontend_supplier')

        # Deleting model 'Product'
        db.delete_table('frontend_product')

        # Deleting model 'Catalog'
        db.delete_table('frontend_catalog')

        # Deleting model 'CatalogIssue'
        db.delete_table('frontend_catalogissue')

        # Deleting model 'CatalogIssueProduct'
        db.delete_table('frontend_catalogissueproduct')

        # Deleting model 'PriceLevelGroup'
        db.delete_table('frontend_pricelevelgroup')

        # Deleting model 'PriceLevel'
        db.delete_table('frontend_pricelevel')

        # Removing M2M table for field products on 'PriceLevel'
        db.delete_table('frontend_pricelevel_products')

        # Deleting model 'Order'
        db.delete_table('frontend_order')

        # Deleting model 'OrderStatus'
        db.delete_table('frontend_orderstatus')

        # Deleting model 'OrderProduct'
        db.delete_table('frontend_orderproduct')

        # Deleting model 'Company'
        db.delete_table('frontend_company')

        # Deleting model 'Invoice'
        db.delete_table('frontend_invoice')


    models = {
        'frontend.catalog': {
            'Meta': {'object_name': 'Catalog'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'})
        },
        'frontend.catalogissue': {
            'Meta': {'object_name': 'CatalogIssue'},
            'catalog': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'issues'", 'to': "orm['frontend.Catalog']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'catalog_issues'", 'symmetrical': 'False', 'through': "orm['frontend.CatalogIssueProduct']", 'to': "orm['frontend.Product']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'})
        },
        'frontend.catalogissueproduct': {
            'Meta': {'object_name': 'CatalogIssueProduct'},
            'catalog_issue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['frontend.CatalogIssue']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img_ref': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'page_ref': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['frontend.Product']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'}),
            'sub_ref': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'})
        },
        'frontend.company': {
            'Meta': {'object_name': 'Company'},
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo_height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'logo_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True'}),
            'logo_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'registration': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'})
        },
        'frontend.customer': {
            'Meta': {'object_name': 'Customer'},
            'address_line_1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'address_line_2': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'Australia'", 'max_length': '100'}),
            'customer_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'delivery_address_line_1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'delivery_address_line_2': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'delivery_attn': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'delivery_country': ('django.db.models.fields.CharField', [], {'default': "'Australia'", 'max_length': '100'}),
            'delivery_postcode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'delivery_state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'delivery_suburb': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'from_src_company_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'from_src_membadd_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'registration': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'frontend.customercontact': {
            'Meta': {'object_name': 'CustomerContact'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contacts'", 'to': "orm['frontend.Customer']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'frontend.importnote': {
            'Meta': {'object_name': 'ImportNote'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'model_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'}),
            'src_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'src_model_id_field': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'src_model_id_text': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50'})
        },
        'frontend.invoice': {
            'Meta': {'object_name': 'Invoice'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['frontend.Company']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'invoices'", 'to': "orm['frontend.Order']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        'frontend.medium': {
            'Meta': {'object_name': 'Medium'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'})
        },
        'frontend.order': {
            'Meta': {'object_name': 'Order'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders'", 'to': "orm['frontend.Customer']"}),
            'discount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '2'}),
            'from_borders_fakeid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'from_src_order_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_address_line_1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'invoice_address_line_2': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'invoice_company_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'invoice_company_reg': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'invoice_country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'invoice_postcode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'invoice_state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'invoice_suburb': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'order_notes': ('django.db.models.fields.CharField', [], {'max_length': '510', 'null': 'True', 'blank': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'+'", 'symmetrical': 'False', 'through': "orm['frontend.OrderProduct']", 'to': "orm['frontend.Product']"}),
            'shipping_address_line_1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'shipping_address_line_2': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'shipping_attn': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'shipping_cost': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'}),
            'shipping_country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'shipping_postcode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'shipping_state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'shipping_suburb': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'}),
            'sp_cost': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '2'}),
            'sub_total': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '2'}),
            'tax': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '2'}),
            'total_cost': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '2'}),
            'wanted_by': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        'frontend.orderproduct': {
            'Meta': {'object_name': 'OrderProduct'},
            'back_order': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'discount_percentage': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'discount_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['frontend.Order']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['frontend.Product']"}),
            'quantity': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'royalty_amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'}),
            'sp_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'}),
            'unit_tax': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'})
        },
        'frontend.orderstatus': {
            'Meta': {'object_name': 'OrderStatus'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'statuses'", 'to': "orm['frontend.Order']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'PS'", 'max_length': '2'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'frontend.pricelevel': {
            'Meta': {'object_name': 'PriceLevel'},
            'block_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cost_per_block': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'cost_per_item': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_amount': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'min_amount': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'price_level_group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'price_levels'", 'null': 'True', 'to': "orm['frontend.PriceLevelGroup']"}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'price_levels'", 'symmetrical': 'False', 'to': "orm['frontend.Product']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'})
        },
        'frontend.pricelevelgroup': {
            'Meta': {'object_name': 'PriceLevelGroup'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'})
        },
        'frontend.product': {
            'Meta': {'object_name': 'Product'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'current_stock': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medium': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': "orm['frontend.Medium']"}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'minimum_stock': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'royalty_img': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': "orm['frontend.RoyaltyImg']"}),
            'size': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['frontend.Size']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'}),
            'sp_cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'products'", 'to': "orm['frontend.Supplier']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'frontend.royaltyimg': {
            'Meta': {'object_name': 'RoyaltyImg'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True'}),
            'image_height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'image_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'percentage': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'})
        },
        'frontend.size': {
            'Meta': {'object_name': 'Size'},
            'depth': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '4'}),
            'height': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'}),
            'sub_notes': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'units': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True'}),
            'width': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '4'})
        },
        'frontend.supplier': {
            'Meta': {'object_name': 'Supplier'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'})
        }
    }

    complete_apps = ['frontend']