# ACC

Airplane Consumption Calculator.

## Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  
- Python3, pip3, virtualenv, postgreqsql>9.6

## 1. Instructions how to use and run it (local deployment).
You have two options to run the current project
1) By using Docker
2) Manually deployment

### 1.1) Using Docker

Start the dev server for local development:
```bash
docker-compose up
```
Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

### 1.2) Manually deployment 
1. install postgresql>9.6 
2. open shell prompt
```bash
sudo su - postgres
psql
```
3. Run the following commands:
```postgresplsql
CREATE DATABASE acc;
CREATE ROLE acc WITH PASSWORD 'acc';
GRANT ALL PRIVILEGES ON DATABASE acc to acc;
ALTER ROLE acc LOGIN CREATEDB;
```
4.Create virtual environment and activate it
```bash
python3 -m virtualenv .venv
soruce /path/to/.venv/bin/activate
```
5. Migrate with database
```bash
./manage.py migrate
```
6. Run the server
```bash
./manage.py runserver
```
7. Check and verify it by opening localhost:8000 in browser

##2. How to check task
You can check it the via [POSTMAN](https://www.getpostman.com/) application 
### 2.1 via Postman

1. Install and open the application
2. Import ACC.postman_collection.json file, which you can find in PROJECT ROOT directory
3. SEND POST Calc method