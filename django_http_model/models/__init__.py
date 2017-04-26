from abc import ABCMeta

from django_http_model.manager import HTTPModelManager
from django_http_model.utils import ClassProperty


class HTTPModel(metaclass=ABCMeta):

    __manager = None

    @ClassProperty
    def objects(self):
        if self.__manager is None:
            self.__manager = HTTPModelManager(self)
        return self.__manager

    class HTTPMeta:
        url = None
        pk_field = None

    def delete(self):
        return self.objects.delete(self.__get_pk())

    def __get_pk(self):
        return getattr(self, self.HTTPMeta.pk_field)
