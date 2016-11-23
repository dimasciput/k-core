# -*- coding: utf-8 -*-
"""Settings for when running under docker in development mode."""
from .utils import ensure_secret_key_file
ensure_secret_key_file()

from .dev import *  # noqa
import os
print os.environ

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'gis',
        'USER': 'docker',
        'PASSWORD': 'docker',
        'HOST': 'db',
        'PORT': 5432,
        'TEST_NAME': 'unittests',
    }
}
