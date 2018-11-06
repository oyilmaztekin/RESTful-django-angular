"""
WSGI config for beyazgezi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

#import os

#from django.core.wsgi import get_wsgi_application

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beyazgezi.settings")

#application = get_wsgi_application()

import os
import sys
import site
from .settings import PRODUCTION, PRODUCT 

if PRODUCTION == True:
	base = "/path/of/your/apache/folder/"
else:
	base = "/path/of/your/local/dev/folder/"

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir(base+'env/lib/python3.6/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append(base)
sys.path.append(base+PRODUCT)
sys.path.append(base+'iletisim')
sys.path.append(base+'sayfalar')
sys.path.append(base+'fotograflar')
sys.path.append(base+'haberler')
sys.path.append(base+'rotalar')
sys.path.append(base+'sayfalar')
sys.path.append(base+'basvur')


os.environ['DJANGO_SETTINGS_MODULE'] = PRODUCT+'.settings'

import django
django.setup()

# Activate your virtual env
activate_env=os.path.expanduser(base+"env/bin/activate_this.py")
#execfile(activate_env, dict(__file__=activate_env))
exec(compile(open(activate_env, "rb").read(), activate_env, 'exec'))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
