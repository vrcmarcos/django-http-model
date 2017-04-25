from abc import ABCMeta

from django_http_model.manager import HTTPModelManager
from django_http_model.utils import ClassProperty


class HTTPModel(metaclass=ABCMeta):

    __manager = None

    @ClassProperty
    def objects(cls):
        if cls.__manager is None:
            cls.__manager = HTTPModelManager(cls)
        return cls.__manager

    class HTTPMeta:
        url = None
