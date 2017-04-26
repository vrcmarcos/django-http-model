from django_http_model.models import HTTPModel, fields


class Company(HTTPModel):

    name = fields.HTTPField()
    company_id = fields.HTTPField(field_name="id")
    founder = fields.HTTPField(field_name="nameOfFounder")
    birthday = fields.HTTPDateField(date_fmt="%Y-%m-%d")

    def __init__(self, name=None, company_id=None, founder=None, birthday=None) -> None:
        super().__init__()
        self.name = name
        self.company_id = company_id
        self.founder = founder
        self.birthday = birthday

    class HTTPMeta(HTTPModel.HTTPMeta):
        url = "http://my.api.com/companies"
        pk_field = "company_id"
