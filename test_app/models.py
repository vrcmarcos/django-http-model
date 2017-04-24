from django_http_model.models import HTTPModel, fields


class Company(HTTPModel):

    name = fields.HTTPStringField(field_name="name")

    class HTTPMeta(HTTPModel.HTTPMeta):
        url = "http://localhost:8000/test_app/companies/"
