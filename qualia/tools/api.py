from tastypie.serializers import Serializer

from tastypie.authentication import Authentication
from tastypie.http import HttpUnauthorized

from django.utils.timezone import is_naive

class ISOSerializer(Serializer):
    """
    Our own serializer to format datetimes in ISO 8601 but with timezone
    offset.
    """
    def format_datetime(self, data):
        # If naive or rfc-2822, default behavior...
        if is_naive(data) or self.datetime_formatting == 'rfc-2822':
            return super(ISOSerializer, self).format_datetime(data)
 
        return data.isoformat()

class KeyOnlyAuthentication(Authentication):
    '''
    Authorises API calls using just the API Key - Likely not perfect,
    but reduces complexity for end developer.
    '''
    def _unauthorized(self):
        return HttpUnauthorized()

    def is_authenticated(self, request, **kwargs):
        from tastypie.models import ApiKey
        api_key = None
        
        try:
            if request.GET:
                api_key = request.GET.get('api_key')    
            elif request.POST:
                api_key = request.POST.get('api_key')

            if api_key:
                key = ApiKey.objects.get(key=api_key)
                request.user = key.user
            else:
                return self._unauthorized()
        except ApiKey.DoesNotExist:
            return self._unauthorized()

        return True