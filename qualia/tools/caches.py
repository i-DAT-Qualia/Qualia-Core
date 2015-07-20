from django.core.cache.backends.memcached import MemcachedCache
import time
import pickle

class LargeMemcachedCache(MemcachedCache):
    "Memcached cache for large objects"

    @property
    def _cache(self):
        if getattr(self, '_client', None) is None:
            self._client = self._lib.Client(self._servers,
                           pickleProtocol=pickle.HIGHEST_PROTOCOL,
                           server_max_value_length = 1024*1024*10)
        return self._client
