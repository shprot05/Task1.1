import psycopg2


def connection():
    conn = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="12345678",
        port="5432",
        dbname="postgres"
    )
    return conn


conn = connection()
cursor = conn.cursor()

# uv,ruff,mypy,env,pydantic_settings
