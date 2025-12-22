import asyncpg
import logging
from typing import AsyncGenerator, Optional

logger = logging.getLogger(__name__)


class DatabaseManager:
    def __init__(self, connection_url: str, min_size: int = 1, max_size: int = 10):
        self.connection_url = connection_url
        self.min_size = min_size
        self.max_size = max_size
        self.pool: Optional[asyncpg.Pool] = None
        self._is_connected = False

    async def connect(self):
        if self._is_connected:
            logger.info("Database is already connected.")
            return
        try:
            self.pool = await asyncpg.create_pool(dsn=self.connection_url, min_size=self.min_size, max_size=self.max_size)
            self._is_connected = True
            logger.info("Database connection pool created.")

        except Exception as e:
            logger.error(f"Failed to connect to database: {e}")
            raise

    async def get_connection(self) -> AsyncGenerator[asyncpg.Connection, None]:
        if not self.pool:
            raise RuntimeError("Database is not connected. Call connect() first.")

        async with self.pool.acquire() as connection:
            try:
                yield connection
            except Exception as e:
                logger.error(f"Database error: {e}")
                raise

    async def disconnect(self):
        if self.pool:
            await self.pool.close()
            self._is_connected = False
            logger.info("Database connection pool closed.")

    @property
    def is_connected(self) -> bool:
        return self._is_connected
