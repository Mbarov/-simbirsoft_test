"""
WSGI config for simbirsoft_test project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise #импорт для выкладывания в сеть (для статических файлов)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simbirsoft_test.settings')

application = get_wsgi_application()
application = DjangoWhiteNoise(application)

