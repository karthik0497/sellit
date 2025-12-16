import yaml
import os
from db_constants import *

# 1. Function to read config
def load_config():
    config_path = db_config_path
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found at {config_path}")
    
    with open(config_path, "r") as f:
        return yaml.safe_load(f)