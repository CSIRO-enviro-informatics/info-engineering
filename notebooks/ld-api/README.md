# info-engineering notebooks
Jupyter notebooks for info engineering

## Pre-requisites
* docker
* docker-compose


## Quickstart
Using a minimal docker stack (python only)
```
$ docker-compose up -d --build
```

Running `docker-compose logs` should give you the session token to use to login via http://localhost:8888

To stop the notebook server:
```
$ docker-compose down -v
```

