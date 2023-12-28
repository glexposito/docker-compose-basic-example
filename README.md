## Getting started

These instructions will get you through the bootstrap phase of creating and deploying containerized applications with Docker Compose.

### Prerequisites

- Make sure that you have Docker and Docker Compose installed
  - Windows or macOS:
    [Install Docker Desktop](https://www.docker.com/get-started)
  - Linux: [Install Docker](https://www.docker.com/get-started) and then
    [Docker Compose](https://github.com/docker/compose)

### Running sample

The root directory contains the `docker-compose.yml` which describes the configuration of service components.

```console
docker compose up
```

#### API
Open http://127.0.0.1:8000/docs to view the automatic API docs in the browser.

#### Web
Open http://127.0.0.1:3000 to view it in the browser.
