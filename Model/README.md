# Flixpredix - Model Server

## Dependencies

To run the Flixpredix server locally, you need to have the following tools installed on your device:

- [Docker](https://docs.docker.com/get-docker/)

## Run locally

### Build server image

```
docker build -t flixpredix/server .
```

### Start server

```
docker run -p 8080:80 flixpredix/server 
```
