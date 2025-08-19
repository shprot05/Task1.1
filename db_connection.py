import psycopg2

from settings import load_settings, ENV_FILE_PATH


def get_connection():
    settings = load_settings(ENV_FILE_PATH)
    conn = psycopg2.connect(
        host=settings.db.host,
        user=settings.db.user,
        password=settings.db.password.get_secret_value(),
        port=settings.db.port,
        dbname=settings.db.name,
    )
    return conn
