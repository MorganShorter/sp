# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'SPUser.email'
        db.alter_column(u'frontend_spuser', 'email', self.gf('django.db.models.fields.EmailField')(max_length=255, unique=True, null=True))

    def backwards(self, orm):

        # Changing field 'SPUser.email'
        db.alter_column(u'frontend_spuser', 'email', self.gf('django.db.models.fields.EmailField')(default='', max_length=255, unique=True))

    models = {
        u'frontend.backorder': {
            'Meta': {'ordering': "('-timestamp',)", 'object_name': 'BackOrder'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'back_orders'", 'to': u"orm['frontend.OrderProduct']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'frontend.catalog': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Catalog'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'frontend.catalogissue': {
            'Meta': {'object_name': 'CatalogIssue'},
            'catalog': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'issues'", 'to': u"orm['frontend.Catalog']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'catalog_issues'", 'symmetrical': 'False', 'through': u"orm['frontend.CatalogIssueProduct']", 'to': u"orm['frontend.Product']"})
        },
        u'frontend.catalogissueproduct': {
            'Meta': {'object_name': 'CatalogIssueProduct'},
            'catalog_issue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.CatalogIssue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img_ref': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'page_ref': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'catalog_links'", 'to': u"orm['frontend.Product']"}),
            'sub_ref': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'})
        },
        u'frontend.company': {
            'Meta': {'object_name': 'Company'},
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo_height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'logo_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True'}),
            'logo_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'registration': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'frontend.customer': {
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_read': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'c_notes'", 'blank': 'True', 'to': u"orm['frontend.Note']"}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'registration': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'telephone_clean': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'frontend.customercontact': {
            'Meta': {'object_name': 'CustomerContact'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contacts'", 'to': u"orm['frontend.Customer']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'frontend.importnote': {
            'Meta': {'object_name': 'ImportNote'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'model_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'src_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'src_model_id_field': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'src_model_id_text': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50'})
        },
        u'frontend.invoice': {
            'Meta': {'object_name': 'Invoice'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['frontend.Company']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'invoices'", 'to': u"orm['frontend.Order']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'frontend.medium': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Medium'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        u'frontend.note': {
            'Meta': {'object_name': 'Note'},
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'frontend.order': {
            'Meta': {'ordering': "('-order_date',)", 'object_name': 'Order'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders'", 'to': u"orm['frontend.Customer']"}),
            'from_borders_fakeid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'from_src_order_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_address_line_1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'invoice_address_line_2': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'invoice_company_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'invoice_company_reg': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'invoice_country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'invoice_postcode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'invoice_state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'invoice_suburb': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'last_read': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'o_notes'", 'symmetrical': 'False', 'to': u"orm['frontend.Note']"}),
            'order_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'order_notes': ('django.db.models.fields.CharField', [], {'max_length': '510', 'null': 'True', 'blank': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'+'", 'symmetrical': 'False', 'through': u"orm['frontend.OrderProduct']", 'to': u"orm['frontend.Product']"}),
            'shipping_address_line_1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'shipping_address_line_2': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'shipping_attn': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'shipping_cost': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'}),
            'shipping_country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'shipping_postcode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'shipping_state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'shipping_suburb': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'total_cost': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '2'}),
            'total_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '2'}),
            'wanted_by': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        u'frontend.orderproduct': {
            'Meta': {'ordering': "('product__code',)", 'object_name': 'OrderProduct'},
            'back_order': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'discount_percentage': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_quantity': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ordered_products'", 'to': u"orm['frontend.Order']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ordered_list'", 'to': u"orm['frontend.Product']"}),
            'quantity': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'}),
            'with_tax': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'frontend.orderstatus': {
            'Meta': {'ordering': "('-timestamp',)", 'object_name': 'OrderStatus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'statuses'", 'to': u"orm['frontend.Order']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'PS'", 'max_length': '2'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.SPUser']", 'null': 'True', 'blank': 'True'})
        },
        u'frontend.pricelevel': {
            'Meta': {'ordering': "('-min_amount',)", 'object_name': 'PriceLevel'},
            'cost_per_item': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_amount': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'min_amount': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'price_levels'", 'null': 'True', 'to': u"orm['frontend.Product']"})
        },
        u'frontend.product': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Product'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'current_stock': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_read': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'manual_royalty': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'medium': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['frontend.Medium']"}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'minimum_stock': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'p_notes'", 'blank': 'True', 'to': u"orm['frontend.Note']"}),
            'royalty_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.RoyaltyGroup']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'size': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'on_delete': 'models.PROTECT', 'to': u"orm['frontend.Size']"}),
            'sp_cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'products'", 'on_delete': 'models.PROTECT', 'to': u"orm['frontend.Supplier']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'frontend.royaltygroup': {
            'Meta': {'ordering': "('name',)", 'object_name': 'RoyaltyGroup'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'royalty': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '2'})
        },
        u'frontend.size': {
            'Meta': {'ordering': "('width', 'height', 'depth', 'units')", 'object_name': 'Size'},
            'depth': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '4'}),
            'height': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'sub_notes': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'units': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True'}),
            'width': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '4'})
        },
        u'frontend.spuser': {
            'Meta': {'object_name': 'SPUser'},
            'bg_color': ('colorfield.fields.ColorField', [], {'default': "'#FFFFFF'", 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'font_color': ('colorfield.fields.ColorField', [], {'default': "'#2B2B2B'", 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'font_size': ('django.db.models.fields.IntegerField', [], {'default': '12', 'null': 'True', 'blank': 'True'}),
            'font_weight': ('django.db.models.fields.CharField', [], {'default': "'normal'", 'max_length': '16', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'jodabrian_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'label_bg_color': ('colorfield.fields.ColorField', [], {'default': "'#EEEEEE'", 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        u'frontend.stockadjust': {
            'Meta': {'ordering': "('-timestamp',)", 'object_name': 'StockAdjust'},
            'added_amount': ('django.db.models.fields.IntegerField', [], {}),
            'current_amount': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stock_adjust'", 'to': u"orm['frontend.Product']"}),
            'reason': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.SPUser']"})
        },
        u'frontend.supplier': {
            'Meta': {'ordering': "('code', 'name')", 'object_name': 'Supplier'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['frontend']