# Django HTTP Model

A Django Manager for HTTP data using the well-known Django ORM interface

[![Build Status](https://travis-ci.org/vrcmarcos/django-http-model.svg?branch=master)](https://travis-ci.org/vrcmarcos/django-http-model) [![Coverage Status](https://coveralls.io/repos/github/vrcmarcos/django-http-model/badge.svg?branch=master)](https://coveralls.io/github/vrcmarcos/django-http-model?branch=master) [![PyPI version](https://badge.fury.io/py/django-http-model.svg)](https://badge.fury.io/py/django-http-model) [![Code Health](https://landscape.io/github/vrcmarcos/django-http-model/master/landscape.svg?style=flat)](https://landscape.io/github/vrcmarcos/django-http-model/master) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/vrcmarcos/django-http-model/master/LICENSE)

## Installation

This package is not in PyPI. We'll add as soon as possible

## Usage

Imagine that you have an endpoint `http://my.api.com/companies` that shows a list of `Companies`:

```json
[
    {
        "name": "Company 1",
        "id": 1,
        "nameOfFounder": "Marcos Cardoso",
        "birthday": "1990-07-30",
    },
    {
        "name": "Company 2",
        "id": 2,
        "nameOfFounder": "Samuel Medeiros Cardoso",
        "birthday": "1955-04-26",
    }
]
```

The first step is create a model class that inherit from `HTTPModel`, and setup the desired attributes and override the `HTTPModel.HTTPMeta` class:

```python
from django_http_model.models import HTTPModel, fields

class Company(HTTPModel):

	name = fields.HTTPField()
	id = fields.HTTPField()
	founder = fields.HTTPField(field_name="nameOfFounder")
	birthday = fields.HTTPDateField(date_fmt="%Y-%m-%d")

	class HTTPMeta(HTTPModel.HTTPMeta):
		url = "http://my.api.com/companies"
```

Now you can call the manager methods from `Company` model: `Company.objects.all()`, for example.


## Implemented methods

- `all/0` (class method)
- `get/1` (class method, params=`{pk: int}`)

## To do

- Relations between `HTTPModel`
- Relations between `HTTPModel` and `django.db.models.Model`
- More manager's methods:
	- `save/0` (instance method)
	- `delete/0` (instance method) and `delete/1` (class method, params=`{pks: list}`)
	- `filter/1` (class method, params=`{pks: list}`) [?]

## Changelog

#### dev:
- **HTTPModel**, **HTTPManager**, **HTTPField** and **HTTPDateField** implemented
- **HTTPManager**: **all** and **get** method implemented
