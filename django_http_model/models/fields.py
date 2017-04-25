class HTTPField:
    field_name = None

    def __init__(self, field_name=None):
        super().__init__()
        self.field_name = field_name


class HTTPDateField(HTTPField):
    date_fmt = None

    def __init__(self, field_name=None, date_fmt="%Y-%m-%d"):
        super().__init__(field_name)
        self.date_fmt = date_fmt
