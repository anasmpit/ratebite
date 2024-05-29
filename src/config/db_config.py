import os

# Database configuration dictionary containing connection parameters.
# User should set environment variables for database credentials (DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT).
# Alternatively, provide credentials directly by assigning values to these variables.
# Example:
#   export DB_NAME='exchange_bi'
#   export DB_USER='username'
#   export DB_PASSWORD='password'
#   export DB_HOST='localhost'
#   export DB_PORT='5432'
# Note: DB_PORT defaults to 5432 if not provided.

DATABASE_CONFIG = {
    'postgres': {
        'dbname': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'port': int(os.getenv('DB_PORT', '5432')),
    }
}
