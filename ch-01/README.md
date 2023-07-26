# StepZen Bootcamp: Setup StepZen

## System Requirements

To install the local dev environment, you need to fulfill the following requirements:

- Either Windows, OSX or Linux as OS
- Node.JS & npm installed. See [link](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).
- Docker or a OCI-conform containerisation tool installed (e.g. Podman).
  - For installing docker, see [link](https://docs.docker.com/engine/install/).
  - For installing podman, see [link](https://podman.io/docs/installation)
- Even if you install a docker alternative as a container tool, you need to install the docker CLI in order to use the stepzen local dev environment. See [Setup using podman](#setup-using-podman) for more information.
- An IDE with GraphQL support. We recommend [VS Code](https://code.visualstudio.com/) with the GraphQL Extension(https://marketplace.visualstudio.com/items?itemName=GraphQL.vscode-graphql)

## Install the StepZen CLI

In order to install the StepZen CLI, execute the following command:

```bash

npm install -g stepzen

```

In case you use `yarn` as your node.js package tool, enter the following command:

```bash

yarn add global stepzen

```

For more information click [here](https://stepzen.com/docs/cli).

## Setup a local dev environment using Docker

For more information click [here](https://stepzen.com/docs/deployment/local-docker).

## Setup a local dev environment using Podman

As stepzen uses the docker CLI to start the local dev environment, you need to
create a connection between podman and docker. This can be achieved by setting 
up the environment variable `DOCKER_HOST` referencing to the created socket.

In current versions of Podman, if you start the vm via the command 
`podman machine start`, the environment variable `DOCKER_HOST` 
will be automatically set:

```bash

API forwarding listening on: /var/run/docker.sock
Docker API clients default to this address. You do not need to set DOCKER_HOST.

```

Podman generates a symbolic link to the socket `/var/run/docker.sock`, which is 
by default in use from the docker cli.
