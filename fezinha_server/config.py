import os

DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_USERNAME = os.environ.get("DB_USERNAME", "user")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")
DB_PORT = int(os.environ.get("DB_PORT", "3306"))
DB_DATABASE = os.environ.get("DB_DATABASE", "fezinha")
ENCRYPT_SECRET_KEY = os.environ.get("ENCRYPT_SECRET_KEY", "ENCRYPT_SECRET_KEY")
HOURS_TO_EXPIRATION_TOKEN = int(os.environ.get("HOURS_TO_EXPIRATION_TOKEN", "12"))
LOG_REPOSITORY = os.environ.get("LOG_REPOSITORY", "../.log/")
HOST_PORT = int(os.environ.get("HOST_PORT", "5000"))
