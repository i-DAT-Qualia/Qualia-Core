from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.utils import timezone

from django.views.decorators.cache import cache_page

def front(request):
    return render_to_response('front.html', {}, context_instance=RequestContext(request))

def terms(request):
    return render_to_response('terms.html', {}, context_instance=RequestContext(request))
