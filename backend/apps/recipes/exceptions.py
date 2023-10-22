class MissingInfo(Exception):
    def __init__(self, *args, **kwargs):
        self.ingredient = kwargs.get('ingredient')
        self.unit = kwargs.get('unit')
        super().__init__(self, *args)
