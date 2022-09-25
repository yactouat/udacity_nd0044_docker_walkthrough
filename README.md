# flask_todo_app_example2

<!-- TOC -->

- [flask_todo_app_example2](#flask_todo_app_example2)
  - [what is this ?](#what-is-this-)
  - [Docker](#docker)
    - [without Docker Compose](#without-docker-compose)
      - [database, volumes and networks](#database-volumes-and-networks)
    - [with Docker Compose](#with-docker-compose)
  - [CI/CD](#cicd)

<!-- /TOC -->

## what is this ?

 a demo app' using Flask with an emphasis on containerisation

## Docker

### without Docker Compose

- to build the image from project root => `docker build -t flask_todos_example_v2:vx.x.x .` (you can check your images with `docker images`)
  - this will not attach the container to any network but the default one
- to run the Flask app' container => `docker run -p 80:5000 --name flask-api flask_todos_example_v2:vx.x.x` (you can check your running containers with `docker ps`)

#### database, volumes and networks

- to persist MySQL data => `docker volume create mysql`
- to persist MySQL config => `docker volume create mysql_config`
- to create a bridge network with DNS lookup so services can talk to each other => `docker network create mysqlnet`
- to create a MySQL instance that will be connected to the app' =>

    ```bash
    docker run --rm -d -v mysql:/var/lib/mysql \
    -v mysql_config:/etc/mysql -p 3306:3306 \
    --network mysqlnet \
    --name mysqldb \
    -e MYSQL_ROOT_PASSWORD=p@ssw0rd1 \
    mysql:5.7.39
    ```

  - the `--rm` flag tells Docker to remove the container when it exits
  - the `-d` flag tells it to run in the background so the user can access the terminal again
  - the `-v` flag tells Docker to bind mount a volume to the container at the specified path
  - the `-e` flag allows to specify an environment variable
- to interact with the DB once it's running => `docker exec -it mysqldb mysql -u root -p`
- to attach the Flask app' container to the same network than the DB =>

  ```bash
  docker run -d \
  --network mysqlnet \
  --name flask-api \
  -p 80:5000 \
  flask_todos_example_v2:vx.x.x
  ```

### with Docker Compose

`docker compose up` will run your whole application stack, simpler right ?

## CI/CD

You can follow along the instructions @ <https://docs.docker.com/language/python/configure-ci-cd/> to configure your CI/CD pipeline
