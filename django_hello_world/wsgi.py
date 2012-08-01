import os
import sys

path = '/var/www/django_examples'
# if path not in sys.path:
sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_hello_world.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
