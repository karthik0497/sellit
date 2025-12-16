import asyncio
import asyncpg
import os
import yaml

from db_constants import *
from py_logging import log_db

# 1. Function to read config
import urllib.parse
from db_helper import load_config

# 2. Main async function to test connection
async def connect_to_db():
    log_db("Loading configuration...")
    config = load_config()
    db_conf = config['database']
    
    # URL encode the password to handle special characters (like '@') safely
    encoded_password = urllib.parse.quote_plus(db_conf['password'])
    
    dsn = f"postgresql://{db_conf['user']}:{encoded_password}@{db_conf['host']}:{db_conf['port']}/{db_conf['db_name']}"
    
    log_db(f"Connecting to: {dsn} ...")
    
    try:
        conn = await asyncpg.connect(dsn)
        log_db("✅ Success! Connected to PostgreSQL.")
        
        version = await conn.fetchval("SELECT version()")
        log_db(f"Database/Version: {version}")
        
        await conn.close()
        log_db("Connection closed.")
        
    except Exception as e:
        log_db(f"❌ Error connecting to database: {e}")

if __name__ == "__main__":
    asyncio.run(connect_to_db())
