#
from cache_manager import CacheManager
import random

class RANDCOPYONE(CacheManager):
    def retrieve_from_caches(self, interest, path):
        content_found_caches = False

        for i in range(0, len(path)):
            p = path[i]
            if self.lookup_cache(p, interest):
                content_found_caches = True
                break
            else:
                pass

        if i != 0:
            self.stats.incr_accepted(self.caches[path[random.randint(0,i)]].store(interest))

        return (content_found_caches, i)
