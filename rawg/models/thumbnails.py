class Thumbnails:
    def __getattr__(self, item):
        return getattr(self, item, None)
