
## Getting Started (Docker Only)

### 1. Prerequisites
- Docker & Docker Compose

### 2. Run the Project
```
# Build and Start everything
docker compose up --build
```
### 3. Check Logs
```
docker logs sellit_app
```

### 4. Start (no rebuild)
```
docker compose up
```

### 5. Start in background
```
docker compose up -d
```

### 6. Stop
```
docker compose down
```
### 7. To remove volumes
```
docker compose down -v
```

### 8. Enter the Postgres Container
```
docker exec -it sellit_postgres sh
```

```
psql -U postgres
```
    