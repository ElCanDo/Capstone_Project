"""
WSGI config for school_management_system project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""


import os
import sys

path = '/home/PrinceN/Capstone_Project/school_management_system'
if path not in sys.path:
    sys.path.append(path)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_management_system.settings')


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
