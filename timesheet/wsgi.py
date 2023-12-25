import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'timesheet.settings')
load_dotenv()

application = get_wsgi_application()
