# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        #"Write your forwards methods here."
        # Note: Remember to use orm['appname.ModelName'] rather than "from appname.models..."
        # Fix state and delivery_state on Customer
        for customer in orm.Customer.objects.all():
            dirty_customer = False
            if customer.state:
                customer.state = customer.state.upper()
                dirty_customer = True
            if customer.delivery_state:
                customer.delivery_state = customer.delivery_state.upper()
                dirty_customer = True

            if dirty_customer:
                customer.save()

        # Fix invoice_state and shipping_state on Order
        for order in orm.Order.objects.all():
            dirty_order = False
            if order.invoice_state:
                order.invoice_state = order.invoice_state.upper()
                dirty_order = True
            if order.shipping_state:
                order.shipping_state = order.shipping_state.upper()
                dirty_order = True

            if dirty_order:
                order.save()


    def backwards(self, orm):
        raise RuntimeError("Cannot reverse this migration.")

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
    symmetrical = True
