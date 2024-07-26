from .base import *
import environ
import psycopg2 # type: ignore

env = environ.Env()

# Read the .env file
environ.Env.read_env()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST', default='localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# Connect to the PostgreSQL database
connection = None
cursor = None
try:
    connection = psycopg2.connect(
        dbname=os.environ.get('DB_NAME'),
        user= os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        host=os.environ.get('DB_HOST', default='localhost'),
        port=os.environ.get('DB_PORT', '5432')
    )
    cursor = connection.cursor()
    print("Database connection successful")

    # Example query
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"Database version: {db_version}")

except Exception as e:
    print(f"Error connecting to database: {e}")

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Database connection closed")

DEBUG = env.bool('DEBUG', default=True)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost', '127.0.0.1', '[::1]'])
