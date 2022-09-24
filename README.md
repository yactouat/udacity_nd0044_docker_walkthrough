# flask_todo_app_example2

<!-- TOC -->

- [flask_todo_app_example2](#flask_todo_app_example2)
    - [what is this ?](#what-is-this-)
    - [Docker](#docker)

<!-- /TOC -->

## what is this ?

 a demo app' using Flask with an emphasis on containerisation

## Docker

- to build the image from project root => `docker build -t flask_demo:vx.x.x .` (you can check your images with `docker images`)
- to run the Flask app' container => `docker run -p 80:5000 --name flask-api flask_demo:vx.x.x` (you can check your running containers with `docker ps`)
