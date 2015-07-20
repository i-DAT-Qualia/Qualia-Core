from django.db import models
import uuid


class UniqueField(models.CharField) :
    '''
    DEPRICATED - use UUIDField in Django 1.8
    '''

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 64 )
        kwargs['blank'] = True
        models.CharField.__init__(self, *args, **kwargs)

    def pre_save(self, model_instance, add):
        if add :
            value = str(uuid.uuid4())[:8]
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(models.CharField, self).pre_save(model_instance, add)
