from django.contrib.auth.models import User

from provider.oauth2.backends import AccessTokenBackend
from provider.oauth2.models import AccessToken

from tools.authentication import OAuth20Authentication

from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response

from functools import wraps

from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def auth_user_from_token(func):
    '''
    Authenicates custom API requests and places user in request object
    '''
    @wraps(func)

    def decorator(request, *args, **kwargs):
        auth_backend = OAuth20Authentication()
        auth_backend.is_authenticated(request)

        if request.user:
            print request.user

        else:
            return render_to_response('success.json', {
                'success': 'False - No Access Token with User',
            }, context_instance=RequestContext(request))


        if not request.user.id:
            return render_to_response('success.json', {
                'success': 'False - No Access Token',
            }, context_instance=RequestContext(request))

        return func(request)

    return decorator


def build_filters(func):
    '''
    Builds filters for dashboards - looks at get variables and passes into request
    '''
    @wraps(func)

    def decorator(request, *args, **kwargs):
        filters = {}

        scope = request.GET.get('scope')
        scope_string = ''

        if 'offer_type' in kwargs:
            filters['offer_type'] = {
                'id':kwargs['offer_type'],
            }

        if 'offer' in kwargs:
            filters['offer'] = {
                'id':kwargs['offer'],
            }

        #default
        if not scope:
            scope = 'A'

        if scope == 'A':
            scope_string = 'City'
        elif scope == 'O':
            scope_string = request.user.org.name

        filters['scope'] = {
            'id':scope,
            'string':scope_string
        }


        time = request.GET.get('time')
        time_string = ''

        if not time:
            time = 'A'

        if time == 'A':
            time_string = 'All Data'
        elif time == '7':
            time_string = 'Last 7 Days'
        elif time == '14':
            time_string = 'Last 14 Days'
        elif time == '28':
            time_string = 'Last 28 Days'

        filters['time'] = {
            'id':time,
            'string':time_string
        }

        request.filters = filters

        return func(request)

    return decorator





def dashboard_level_required(view_func, user_level=2, redirect_field_name=REDIRECT_FIELD_NAME):
    '''
    Based on staff_member_required, checks if user is of high enough level to access the dashboard
    '''
    return user_passes_test(
        lambda u: u.is_active and (u.user_level >= user_level),
        redirect_field_name=redirect_field_name
    )(view_func)
