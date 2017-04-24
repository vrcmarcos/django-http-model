import json

import requests


class HTTPModelManager:

    meta = None
    model = None

    def __init__(self, model) -> None:
        super().__init__()
        self.model = model
        self.meta = model.HTTPMeta

    def all(self):
        response = requests.get(self.meta.url)
        result = []
        if response.ok:
            for item_dict in json.loads(response.text):
                instance = self.model()
                for attribute, value in item_dict.items():
                    if hasattr(instance, attribute):
                        setattr(instance, attribute, value)
                result.append(instance)
        return result
