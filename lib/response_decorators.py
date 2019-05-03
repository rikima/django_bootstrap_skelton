<<<<<<< HEAD
import csv

from django.http import HttpResponse
from django.template import Context, loader
=======
import sys
import csv
from datetime import datetime

from django.http import HttpResponse
from django.template import Context, loader
from django.utils import simplejson
>>>>>>> origin/master

debug = True

def csv_response():
    def deco(func):
        def new(*args, **opts):
            context = func(*args, **opts)
            
            csvdata = context['csvdata']
            filename = context['filename']
            
            response = HttpResponse(mimetype='text/csv')
            response['Content-Disposition'] = 'attachment; filename=%s' %(filename)
            
            writer = csv.writer(response)
            for d in csvdata:
                writer.writerow(d)

            return response
        return new 
    return deco



def rss_response(template):
    def deco(func):

        def new(*args, **opts):
            context = func(*args, **opts)
            t = loader.get_template(template)
            hr = HttpResponse(t.render(context), mimetype='application/rss+xml; charset=utf-8')
            
            return hr
        
        return new 

    return deco


def xml_response(template):
    def deco(func):

        def new(*args, **opts):
            context = func(*args, **opts)
            t = loader.get_template(template)
            hr = HttpResponse(t.render(context), mimetype="text/xml")
            return hr
        
        return new 

    return deco


def http_response(template):
    def deco(func):
        def new(*args, **opts):
            context = func(*args, **opts)
            t = loader.get_template(template)
            return HttpResponse(t.render(context))

        return new 

    return deco

def _post_param(request, param_name, default=None):
    return request.POST.get(param_name, default=default)

def _get_param(request, param_name, default=None):
    return request.GET.get(param_name, default=default)

<<<<<<< HEAD
def _get_param_as_int(request, param_name, default=0):
    return int(request.GET.get(param_name, default=default))
    
=======


def _get_param_as_int(request, param_name, default=0):
    return int(request.GET.get(param_name, default=default))
    

    
>>>>>>> origin/master
def _http_response(template, context):
    t = loader.get_template(template)
    return HttpResponse(t.render(context))
