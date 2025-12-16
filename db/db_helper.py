import yaml
import os
from db_constants import *

def load_config():
    # Priority: Env Vars > Constants
    return {
        'database': {
            'host': os.getenv('DB_HOST', host),
            'port': os.getenv('DB_PORT', port),
            'user': os.getenv('DB_USER', user),
            'password': os.getenv('DB_PASSWORD', password),
            'db_name': os.getenv('DB_NAME', db_name)
        }
    }