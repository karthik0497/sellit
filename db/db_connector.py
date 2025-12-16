
import asyncio
import asyncpg
import os



# 2. Main async function to test connection
async def connect_to_db():
    print("Loading configuration...")
    config = load_config()
    db_conf = config['database']
    
    dsn = f"postgresql://{db_conf['user']}:{db_conf['password']}@{db_conf['host']}:{db_conf['port']}/{db_conf['db_name']}"
    
    print(f"Connecting to: {dsn} ...")
    
    try:
        # Create a connection
        conn = await asyncpg.connect(dsn)
        print("✅ Success! Connected to PostgreSQL.")
        
        # Run a simple query
        version = await conn.fetchval("SELECT version()")
        print(f"Database/Version: {version}")
        
        await conn.close()
        print("Connection closed.")
        
    except Exception as e:
        print(f"❌ Error connecting to database: {e}")

# 3. Entry point
if __name__ == "__main__":
    asyncio.run(connect_to_db())
