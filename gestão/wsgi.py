"""
WSGI config for gestão project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from d

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestão.settings.base')

application = get_wsgi_application()
