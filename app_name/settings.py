import os

# Current Directory
DIR = os.path.join(os.getcwd())

APP_NAME = 'APP_NAME'

# Database configuration
DB_ENGINE = os.getenv("DB_ENGINE", default='sqlite')


DB_NAME = os.getenv("DB_NAME", default=APP_NAME)
DB_USER = os.getenv("DB_USER", default='shamaru')
DB_PASS = os.getenv("DB_PASS", default='shamarups3')
DB_HOST = os.getenv("DB_HOST", default='locahost')
DB_PORT = os.getenv("DB_PORT", default=None)

DATABASE_CONFIG = {
    'user': DB_USER,
    'pw': DB_PASS,
    'db': DB_NAME,
    'host': DB_HOST,
    'port': DB_PORT,
    'sqlite_filename': '%s.db' % APP_NAME
}

DATABASE_URLS = {
    'postgres': 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % DATABASE_CONFIG,
    'mysql': 'mysql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % DATABASE_CONFIG,
    'oracle': 'oracle://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % DATABASE_CONFIG,
    'sqlite': 'sqlite:///%s' % os.path.join(DIR, APP_NAME, DATABASE_CONFIG['sqlite_filename'])
}

DEBUG = os.getenv('FLASK_DEBUG', default=1)

if not DB_ENGINE in DATABASE_URLS:
    raise Exception('DB ENGINE IS NOT SUPPORTED')
