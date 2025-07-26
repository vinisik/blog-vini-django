import os
import sys

# Adiciona a raiz do projeto ao sys.path
sys.path.append(os.path.dirname(__file__) + '/../')

# Define o settings.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projects.settings")

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()
