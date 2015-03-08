from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from django.views.decorators.csrf import csrf_exempt

import json

from qualia.accounts.models import QualiaUser

from provider.oauth2.backends import BasicClientBackend, RequestParamsClientBackend
from provider.oauth2.models import AccessToken
from provider.views import AccessToken as AccessTokenView

import provider.scope

from django.contrib.auth import authenticate, login
from qualia.tools.decorators import auth_user_from_token


@csrf_exempt
def register_user(request):

    success = False
    auth_backend = RequestParamsClientBackend()
    client = auth_backend.authenticate(request)

    if client:
        if request.method == "POST":

            if QualiaUser.objects.filter(email=request.POST['email']).count():
                success = 'False - Email exists'

            else:
                user = QualiaUser.objects.create_user(request.POST['email'], request.POST['password'])
                token = AccessToken.objects.create(
                    user=user,
                    client=client,
                    scope=provider.scope.to_int(request.POST['scope'])
                )
                success = True

                token_view = AccessTokenView()

                return token_view.access_token_response(token)

    return render_to_response('success.json', {
        'success': success,
    }, context_instance=RequestContext(request))


@csrf_exempt
def login_user(request):

    success = False
    auth_backend = RequestParamsClientBackend()
    client = auth_backend.authenticate(request)

    if client:
        if request.method == "POST":

            user = authenticate(email=request.POST['email'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    # Redirect to a success page.
                    token = AccessToken.objects.create(
                        user=user,
                        client=client,
                        scope=provider.scope.to_int(request.POST['scope'])
                    )

                    success = True

                    token_view = AccessTokenView()

                    return token_view.access_token_response(token)
                else:
                    # Return a 'disabled account' error message
                    success = 'False - Account disabled'
            else:
                # Return an 'invalid login' error message.
                success = 'False - Invalid login'

    return render_to_response('success.json', {
        'success': success,
    }, context_instance=RequestContext(request))


@csrf_exempt
@auth_user_from_token
def logout_user(request):
    key = request.META['oauth_consumer_key']
    token = get_object_or_404(AccessToken, token=key)
    token.delete()

    data_return = {
        'success': True,
        'message': 'Logged Out'
    }

    return JsonResponse(data_return, safe=False)
