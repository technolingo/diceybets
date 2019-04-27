import os
basedir = os.path.abspath(os.path.dirname(__file__))


DEBUG = False
TESTING = False
CSRF_ENABLED = True
SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
