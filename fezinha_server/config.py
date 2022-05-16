import os

DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_USERNAME = os.environ.get("DB_USERNAME", "user")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")
DB_PORT = int(os.environ.get("DB_PORT", "3306"))
DB_DATABASE = os.environ.get("DB_DATABASE", "fezinha")
