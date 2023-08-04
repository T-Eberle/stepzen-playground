# Local development environment

# Getting started:

## Network

Make sure the services are in the same network as the stepzen-local container. Its the container based on us-docker.pkg.dev/stepzen-public/images/stepzen image. 
With `docker inspect $(container_id)` you can see the network name of the stepzen container. It's usually `stepzen-network`

Add the network to the compose file:
`
networks:
  stepzen-network:
    external:
      true
`

and the network to the service in compose file
`
  agile-api:
    build: ./agile-api
    ports:
      - 18080:8080
    networks: 
      - stepzen-network
`