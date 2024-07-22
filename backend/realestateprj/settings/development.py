from .base import os
import environ
import psycopg2 # type: ignore

# Initialize environment variables
env = environ.Env()


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST', default='localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# Connect to the PostgreSQL database
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
