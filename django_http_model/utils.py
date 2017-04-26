import json
import urllib

import requests


class ClassProperty(property):
    """
    Thanks http://stackoverflow.com/a/7864317 !
    """

    def __get__(self, cls, owner):
        return classmethod(self.fget).__get__(None, owner)()


class RequestUtils(object):

    @staticmethod
    def get(url, pk=None):
        if pk is not None:
            url = RequestUtils.__mount_url(url, pk)
        response = requests.get(url)
        result = None
        if response.ok and response.text is not None and response.text != "":
            result = json.loads(response.text)
        return result

    @staticmethod
    def delete(url, pk):
        url = RequestUtils.__mount_url(url, pk)
        response = requests.delete(url)
        return response.ok

    @staticmethod
    def __mount_url(url, pk):
        return urllib.parse.urljoin("{0}/".format(url), str(pk))
