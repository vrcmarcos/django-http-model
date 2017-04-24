from abc import ABCMeta


class HTTPField(metaclass=ABCMeta):
    field_name = ""

    def __init__(self, field_name) -> None:
        super().__init__()
        self.field_name = field_name


class HTTPStringField(HTTPField):
    pass
