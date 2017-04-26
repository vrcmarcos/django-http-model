import time

from django_http_model.models import fields
from django_http_model.utils import RequestUtils


class HTTPModelManager:

    meta = None
    model = None

    def __init__(self, model):
        super().__init__()
        self.model = model
        self.meta = model.HTTPMeta

    def all(self):
        result = []
        response = RequestUtils.get(self.meta.url)
        if response is not None:
            for instance_attributes_dict in response:
                instance = self.__create_instance(instance_attributes_dict)
                result.append(instance)
        return result

    def get(self, pk):
        response = RequestUtils.get(self.meta.url, pk)
        return None if response is None else self.__create_instance(response)

    def delete(self, pk):
        return RequestUtils.delete(self.meta.url, pk)

    def __create_instance(self, instance_attributes_dict):
        instance = self.model()
        for attribute, value in self.model.__dict__.items():
            if isinstance(value, fields.HTTPField):
                field_name = getattr(value, "field_name")

                if field_name is None:
                    field_name = attribute

                if field_name in instance_attributes_dict:
                    instance_attribute_value = instance_attributes_dict[field_name]

                    if isinstance(value, fields.HTTPDateField):
                        date_fmt = getattr(value, "date_fmt")
                        instance_attribute_value = time.strptime(instance_attribute_value, date_fmt)

                    setattr(instance, attribute, instance_attribute_value)

        return instance
