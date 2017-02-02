#!/usr/bin/python2.6
import sys, os
os.environ['PYTHON_EGG_CACHE'] = "/var/www/u0298475/data/www/chernoe-zerkalo.ru/mirror/.python-eggs"
# Add a custom Python path.
# sys.path.insert(0, "/var/www/u0298475/data/www/chernoe-zerkalo.ru/env/lib/python2.6/site-packages/")
sys.path.insert(0, "/var/www/u0298475/data/www/chernoe-zerkalo.ru/mirror/")
sys.path.insert(0, "/var/www/u0298475/data/www/chernoe-zerkalo.ru/mirror/mirror/")
# Switch to the directory of your project. (Optional.)
os.chdir("/var/www/u0298475/data/www/chernoe-zerkalo.ru/mirror/mirror/")
# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "mirror.settings"
from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
