import os
import sys


sys.path.append('/home/server/AnarWeb/')

os.environ['PYTHON_EGG_CACHE'] = '/home/server/AnarWeb/.python-egg'
os.environ['DJANGO_SETTINGS_MODULE'] = 'anar.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()