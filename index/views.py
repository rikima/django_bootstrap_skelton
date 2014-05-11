from django.shortcuts import render
from django.template import Context, loader
from django.contrib.auth import logout

from lib.http_decorators import http_response

@http_response('base.html')
def index(request):
    c = Context(dict())
    return c

