"""
WSGI config for repromatch project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "repromatch.settings")
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
