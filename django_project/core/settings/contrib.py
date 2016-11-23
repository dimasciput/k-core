# coding=utf-8
"""
core.settings.contrib
"""
# needed so cartridge gets correct currency
import locale
import os
from .base import *  # noqa

# Store these package names here as they may change in the future since
# at the moment we are using custom forks of them.
PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"
GRAPPELLI_INSTALLED = True

# Extra installed apps - grapelli needs to be added before others
INSTALLED_APPS += (
)

GRAPPELLI_ADMIN_TITLE = 'Site administration panel'

