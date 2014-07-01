import json
from django.http import HttpResponse
from django.template import loader, RequestContext


def json_response(data):
    return HttpResponse(json.dumps(data), content_type='application/json')


def __preprocess_get_request(request, pk, model):
    error = None
    obj = None

    if request.method == 'POST':
        params = request.POST
    elif request.method == 'GET':
        params = request.GET
    else:
        params = {}

    if not pk and 'id' in params:
        pk = params['id']

    if pk:
        try:
            obj = model.objects.get(pk=pk)
        except model.DoesNotExist:
            error = 'No %s found with id %s' % (model.__class__.__name__, pk)
    else:
        error = 'No primary key given to find %s' % model.__class__.__name__

    return pk, params, obj, error


def __taco_render(request, template, context):
    taco_controlplate = loader.get_template(template)
    c_royal = RequestContext(request, context)
    return HttpResponse(taco_controlplate.render(c_royal), content_type='application/xml')


def phone_for_search(s):
    return str(s).translate(None, '-_ ,.[]()')