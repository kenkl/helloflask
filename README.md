#  helloflask

This is a very minimal Docker image with Flask.

The purpose is to have a simple listener on a Docker host to validate basic traffic-flow to the container.

The Docker host (or wherever you build the image) will need docker-compose to build from this source tree. Alternately, I do have this hosted on [Docker Hub](https://hub.docker.com/repository/docker/kenkl/helloflask) as a public image, so if you're so inclined, it can be pulled/run from there without building anything:

```
docker run -d -p 8080:5000 --name=helloflask kenkl/helloflask
```


