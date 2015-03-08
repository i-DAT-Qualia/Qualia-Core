from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, redirect

def reset_password_page(request):
    return redirect('/accounts/password/reset/')
