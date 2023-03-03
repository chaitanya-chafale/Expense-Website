"""
WSGI config for expensewebsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'expensewebsite.settings')

application = get_wsgi_application()


# import os
# from django.conf import settings
# from django.contrib.staticfiles.handlers import StaticFilesHandler
# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
# if settings.DEBUG:
#     application = StaticFilesHandler(get_wsgi_application())
# else:
#     application = get_wsgi_application()