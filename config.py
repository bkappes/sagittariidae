import os

WTF_CSRF_ENABLED = True
SECRET_KEY = ']`<{e&b$D5)tzd)>242KyFGz8jEZzk8:'

THREADS_PER_PAGE = 8

UPLOAD_PATH = '/mnt/adapt/'

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
