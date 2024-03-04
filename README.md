# Project Movies application

## Start
...
## <span style='color:red'>Installing</span>

### <span style='color:yellow'>Instal Deps</span>
```bash
# install pipenv
pip install pipenv

# activate virtual env
pipenv shell

# install deps
pipenv sync --dev
```
### <span style='color:yellow'>Collecting static files</span>
```bash
# copy all static files to the directory "staticfiles" 
python src/manage.py collectstatic
```

### Additional

```bash
# regenerate Pipfile.lock file
pipenv lock

# pipenv lock & pipenv sync
pipenv update
```


### Run application
```bash
# copy the default environment file to create your own configuration file:
cp .env.default .env,

# edit the .env file and set the PostgreSQL host to "localhost":
POSTGRES_HOST = "localhost"

# perform migrations
python src/manage.py migrate

# create superuser
python src/manage.py createsuperuser

# run django development server
python src/manage.py runserver

# alternative run application with gunicorn wsgi server
gunicorn src.config.wsgi -c gunicorn_config.py
```
## <span style='color:red'>Run the application from the Docker using Docker Compose</span>


```bash
# copy the default environment file to create your own configuration file:
cp .env.default .env,

# edit the .env file and set the PostgreSQL host to "postgres":
POSTGRES_HOST = "postgres"

# Build the application image
docker-compose build

# Run docker-compose services as deaemon
docker-compose up -d

# to connect to the Docker container.
docker exec -it movies_app bash

# perform migrations
python src/manage.py migrate

# create superuser
python src/manage.py createsuperuser
```

### Usefull commands

```bash
# Build images
docker-compose build

# Stop containers
docker-compose down

# Restart containers
docker-compose restart

# Check containers status
docker-compose ps
```

### Logs
```bash
# get all logs
docker-compose logs

# get specific logs
docker-compose logs app

# get limited logs
docker-compose logs --tail 10 app

# get flowed logs
docker-compose logs -f app
```
## Usage code quality tools
The pre-commit hook will be automatically run