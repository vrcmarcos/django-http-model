# Django HTTP Model

A Django Manager for HTTP data

[![Build Status](https://travis-ci.org/vrcmarcos/django-http-model.svg?branch=master)](https://travis-ci.org/vrcmarcos/django-http-model) [![Coverage Status](https://coveralls.io/repos/github/vrcmarcos/django-http-model/badge.svg?branch=master)](https://coveralls.io/github/vrcmarcos/django-http-model?branch=master) [![PyPI version](https://badge.fury.io/py/django-http-model.svg)](https://badge.fury.io/py/django-http-model) [![Code Health](https://landscape.io/github/vrcmarcos/django-http-model/master/landscape.svg?style=flat)](https://landscape.io/github/vrcmarcos/django-http-model/master) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/vrcmarcos/django-http-model/master/LICENSE)

## Installation

```bash
pip install django-http-model
```

## Usage

Make your model inherit from `HTTPModel`:

```python
from django_http_model.models import HTTPModel, fields

class MyModel(HTTPModel):

	string_property = fields.HTTPStringField(field_name="field")

	class HTTPMeta(HTTPModel.HTTPMeta):
    	url = "http://my.api.com/model_list_endpoint/"
```

## Changelog

#### dev:
- **HTTPModel**, **HTTPStringField** and **HTTPManager** implemented