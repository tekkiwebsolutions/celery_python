from django.core.servers.basehttp import WSGIServer
from django.core.wsgi import get_wsgi_application
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

application = get_wsgi_application()
server = WSGIServer(("localhost", 8001), application)  # Corrected argument passing
print('Starting WSGI server on http://localhost:8001')
server.serve_forever()