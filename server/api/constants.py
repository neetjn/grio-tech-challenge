DB_NAME = os.environ.get('DB_NAME', 'user_search_app')
DB_HOST = os.environ.get('DB_HOST', '127.0.0.1')
DB_PORT = os.environ.get('DB_PORT', 5432)
DB_USER = os.environ.get('DB_USER', None)
DB_PASS = os.environ.get('DB_PASS', None)

BOOTSTRAP = os.environ.get('BOOTSTRAP', False)
