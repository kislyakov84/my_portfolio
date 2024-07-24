import os
import sys
sys.path.append('/opt/build')
sys.path.append('/opt/build/my_portfolio')
sys.path.append('/opt/build/my_portfolio/my_portfolio')

from django.core.wsgi import get_wsgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_portfolio.my_portfolio.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')

application = get_wsgi_application()
