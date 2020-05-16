class Ratings(object):
    def __getattr__(self, item):
        return getattr(self, item, None)
