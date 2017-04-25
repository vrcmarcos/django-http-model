import json
import urllib

import requests


class ClassProperty(property):
    """
    Thanks http://stackoverflow.com/a/7864317 !
    """

    def __get__(self, cls, owner):
        return classmethod(self.fget).__get__(None, owner)()


class RequestUtils:

    @staticmethod
    def fetch_from_url(url, path_to_append=None):
        if path_to_append is not None:
            url = urllib.parse.urljoin("{0}/".format(url), str(path_to_append))
        response = requests.get(url)
        result = None
        if response.ok:
            result = json.loads(response.text)
        return result
