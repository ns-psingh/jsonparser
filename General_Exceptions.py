
class VerticalFlattenException(Exception):

    def __init__(self, error_type):
        self.error_type = error_type

    def __str__(self):
        return(repr(self.error_type))

