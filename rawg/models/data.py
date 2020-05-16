class Data:
    def __getattr__(self, item):
        return getattr(self, item, None)
