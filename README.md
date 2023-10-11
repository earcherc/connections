# Dashboard

This template provides a foundation for a NextJs dashboard using FastApi and Docker


## Planning Doc
- [Google Docs](https://docs.google.com/document/d/1OTwHx2cQ_MdIOylIY77iquLv_W90QJleSebXlGf27o8/edit?usp=sharing)

## Backend 
### Deps
- homebrew/nix (package manager)
- direnv
- docker-compose
- docker desktop (default)/colima
    - colima ipv6 issue https://github.com/abiosoft/colima/issues/583

### Local Development
1. `cd <root_project_folder>/`
2. `cd backend/`
3. `python3 -m venv venv`
4. remove `.sample` from `.envrc.sample` and replace defaults
5. `direnv allow` from backend root dir
6. Install requirements for `venv`
```
pip install -r requirements.txt
```

7.  Use VSCode workspace to open project, then set interpreter path for each workspace venv (unless vscode correctly interprets)

### Docker
1. Start Docker daemon (colima or default docker desktop)
2. Navigate to root `backend/`
3. Start docker process with docker-compose (w/wo `--build`):
```
docker-compose up --build
```

### Useful Docker commands
```
docker exec -it <postgres_db_container_id> psql -U <username> -d <db_name: auth_db/core_db>
docker exec -it <container_id> alembic revision --autogenerate -m "Migration message goes here"
docker exec -it <container_id> alembic upgrade head
docker exec -it <container_id> alembic downgrade -1
docker exec -it <container_id> env
docker exec -it <container_id> /bin/bash

docker-compose restart <service_name>
docker-compose build <service_name>
docker-compose up -d --no-deps --force-recreate <service_name>
docker-compose down
docker logs -f <container_id>
docker-compose logs <service_name: db>
docker volume rm <volume_name>
docker volume ls
docker image ls
docker image prune
docker image prune -a
docker ps
apt-get update && apt-get install curl (install curl in container)
```

`docker exec -it` - exec commands in a running container (it~>interact)

### DBeaver Connection Settings

To configure your PostgreSQL database connection in DBeaver, use the following settings:

- **Database**: PostgreSQL
- **Show All Databases**: Check this option

##### Connection Parameters:

| Parameter  | Value            | Description                 |
|------------|------------------|-----------------------------|
| Host       | `0.0.0.0`        | Host address                |
| Port       | `5432`           | Port number                 |
| Database   | `EMPTY`          | Leave this field empty      |
| Username   | `<POSTGRES_USER>`| Replace with actual username|
| Password   | `<POSTGRES_PASSWORD>`| Replace with actual password|
