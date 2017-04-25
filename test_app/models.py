from django_http_model.models import HTTPModel, fields


class Company(HTTPModel):

    name = fields.HTTPField()
    company_id = fields.HTTPField(field_name="id")
    founder = fields.HTTPField(field_name="nameOfFounder")
    birthday = fields.HTTPDateField(date_fmt="%Y-%m-%d")

    class HTTPMeta(HTTPModel.HTTPMeta):
        url = "http://localhost:8000/test_app/companies/"
