import json
from django.views.generic import ListView
from django.core import serializers
from django.contrib.auth.decorators import login_required

from ..models import Product, PriceLevel, CatalogIssueProduct
from ..mixins import TacoMixin
from ..utils import __preprocess_get_request, __taco_render, json_response
from .. import formfields


class ProductList(TacoMixin, ListView):
    model = Product
    template_name = 'taconite/product/list.xml'

    def get_queryset(self):
        qs = super(ProductList, self).get_queryset()
        fltr = {}
        if self.request.GET.get('product_code', None):
            fltr['code__istartswith'] = self.request.GET['product_code']

        if self.request.GET.get('find_product_name', None):
            fltr['name__icontains'] = self.request.GET['find_product_name']

        if self.request.GET.get('issue_id', None):
            fltr['catalog_links__catalog_issue_id'] = self.request.GET['issue_id']

            if self.request.GET.get('issue_page', None):
                if self.request.GET['issue_page'].isdigit():
                    fltr['catalog_links__page_ref'] = self.request.GET['issue_page']

            if self.request.GET.get('issue_img', None):
                if self.request.GET['issue_img'].isdigit():
                    fltr['catalog_links__img_ref'] = self.request.GET['issue_img']

            if self.request.GET.get('issue_sub', None):
                if self.request.GET['issue_sub'].isdigit():
                    fltr['catalog_links__sub_ref'] = self.request.GET['issue_sub']

        if not fltr:
            if self.request.GET.get('last', None):
                return qs.order_by('-last_read')[:10]
            else:
                return qs.none()

        return qs.filter(**fltr)


product_list = ProductList.as_view()


@login_required
def product_get(request, pk):
    pk, params, obj, error = __preprocess_get_request(request, pk, Product)
    fields = formfields.ProductForm(obj)
    obj.save()  # update last_read

    return __taco_render(request, 'taconite/product/item.xml', {
        'error': error,
        'fields': fields,
        'obj': obj,
        'only_list': bool(request.GET.get('only_list', False)),
    })


@login_required
def product_save(request):
    msg = ''
    new_obj = False
    obj_id = None
    saved = False
    try:
        for obj in serializers.deserialize('json', request.body):
            if obj.object.__class__ == Product:
                if not obj.object.id:
                    new_obj = True
                    obj.save()
                    saved = True
                    try:
                        PriceLevel(
                            product=obj.object,
                            min_amount=1,
                            cost_per_item=obj.object.sp_cost
                        ).save()
                    except Exception, e:
                        print 'Error product_save [103]'
                        pass
                    msg = 'Product created (ID:%d)' % obj.object.id

                else:
                    obj.save()
                    saved = True
                    msg = 'Product saved'

                obj_id = obj.object.id
            else:
                msg = 'Did not receive expected object Product. You sent me a %s' % obj.object.__class__.__name__

    except Exception, e:
        msg = 'Wrong values'
        print 'Error %s' % e

    return json_response({
        'saved': saved,
        'msg': msg,
        'obj_id': obj_id,
        'created': True if new_obj else False
    })


@login_required
def product_price_get(request, prod_id, price_id):
    pk, params, obj, error = __preprocess_get_request(request, price_id, PriceLevel)

    if int(prod_id) != obj.product_id:
        obj = None
        error = 'Wrong PK'

    fields = formfields.PriceLevelForm(obj)
    return __taco_render(request, 'taconite/product/price_level.xml', {
        'error': error,
        'fields': fields,
        'obj': obj,
        'prod_id': prod_id,
    })


@login_required
def product_price_save(request):
    msg = ''
    new_obj = False
    obj_id = None
    saved = False
    try:
        for obj in serializers.deserialize('json', request.body):
            if obj.object.__class__ == PriceLevel:
                if not obj.object.id:
                    new_obj = True

                if obj.object.max_amount:
                    if obj.object.min_amount >= obj.object.max_amount and not obj.object.block_only:
                        msg = 'Max Qty should be bigger than Min Qty (if it doesn`t a block)'
                        break
                else:
                    obj.object.max_amount = None

                obj.save()
                obj_id = obj.object.id
                saved = True

                if new_obj:
                    msg = 'Product price level created (ID:%d)' % obj.object.id
                else:
                    msg = 'Product price level saved'
            else:
                msg = 'Did not receive expected object PriceLevel. You sent me a %s' % obj.object.__class__.__name__

    except Exception, e:
        msg = 'Wrong values'
        print e

    return json_response({
        'msg': msg,
        'obj_id': obj_id,
        'created': True if new_obj else False,
        'saved': saved
    })


@login_required
def product_price_delete(request, prod_id, price_id):
    try:
        pl = PriceLevel.objects.get(
            pk=price_id,
            product_id=int(prod_id)
        )
    except PriceLevel.DoesNotExist:
        return json_response({
            'status': 'error',
            'msg': 'Wrong ID'
        })

    pl.delete()

    return json_response({
        'status': 'ok',
        'msg': 'PriceLevel has deleted!'
    })

'''
Catalog issue link

'''
@login_required
def product_issue_get(request, prod_id, issue_id):
    pk, params, obj, error = __preprocess_get_request(request, issue_id, CatalogIssueProduct)

    if int(prod_id) != obj.product_id:
        obj = None
        error = 'Wrong PK'

    fields = formfields.ProductIssueForm(obj)
    return __taco_render(request, 'taconite/product/issue.xml', {
        'error': error,
        'fields': fields,
        'obj': obj,
        'prod_id': prod_id,
    })


@login_required
def product_issue_save(request):
    msg = ''
    new_obj = False
    obj_id = None
    saved = False
    try:
        for obj in serializers.deserialize('json', request.body):
            if obj.object.__class__ == CatalogIssueProduct:
                if not obj.object.id:
                    new_obj = True

                obj.save()
                obj_id = obj.object.id
                saved = True

                if new_obj:
                    msg = 'Issue link created (ID:%d)' % obj.object.id
                else:
                    msg = 'Issue link saved'
            else:
                msg = 'Did not receive expected object CatalogIssueProduct. You sent me a %s' % obj.object.__class__.__name__

    except Exception, e:
        msg = 'Wrong values'
        print e

    return json_response({
        'msg': msg,
        'obj_id': obj_id,
        'created': True if new_obj else False,
        'saved': saved
    })


@login_required
def product_issue_delete(request, prod_id, issue_id):
    try:
        pl = CatalogIssueProduct.objects.get(
            pk=issue_id,
            product_id=int(prod_id)
        )
    except CatalogIssueProduct.DoesNotExist:
        return json_response({
            'status': 'error',
            'msg': 'Wrong ID'
        })

    pl.delete()

    return json_response({
        'status': 'ok',
        'msg': 'Catalog link has deleted!'
    })


@login_required
def product_stock_adjust(request, prod_id):
    try:
        product = Product.objects.get(
            pk=prod_id,
        )
    except Product.DoesNotExist:
        return json_response({
            'status': 'error',
            'msg': 'Wrong ID'
        })

    print 'stock: %s' % product.current_stock

    data = json.loads(request.body)
    try:
        product.stock_adjust.create(
            reason=int(data['reason']),
            current_amount=product.current_stock,
            added_amount=int(data['amount']),
            user=request.user
        )
    except Exception, e:
        print 'Error (product_stock_adjust): %s' % e
        return json_response({
            'status': 'error',
            'msg': 'Bad data'
        })

    return json_response({
        'status': 'ok',
        'msg': 'Amount added to current stock',
        'current_stock': product.current_stock
    })