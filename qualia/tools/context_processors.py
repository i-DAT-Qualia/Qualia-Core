from django.conf import settings

def branding(request):
    return {
        'APP_NAME': settings.APP_NAME,
        'QUALIA_NAME': settings.QUALIA_NAME,
        'LOGO': settings.LOGO,
        'FAVICON': settings.FAVICON
    }