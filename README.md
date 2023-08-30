# StepZen & GraphQL Bootcamp

- [Chapter 1: Setup and Installation](ch-01/README.md)
- [Chapter 2: Create and Prepare](ch-02/README.md)
- [Chapter 3: Generate and Connect](ch-03/README.md)
- [Chapter 4: Combine and mutuate](ch-04/README.md)
- [Chapter 5: Extend](ch-05/README.md)
- [Chapter 6: Queries and Fragments](ch-06/README.md)
- [Chapter 7: Mocking and Testing](ch-07/README.md)



## Prepare the environment

For the test/bootcamp environment, an OCI conform container-tool is required. 
Furthermore, you need to be able to execute `docker-compose` files.
There are several options to run a `docker-compose`-file:

- Docker Compose: [More](https://docs.docker.com/compose/)
- Podman Compose: [More](https://github.com/containers/podman-compose)

If these requirements are fulfilled, you can start the environment 
depending on your OCI-tool.

For Docker:

```bash
docker-compose up --force-recreate --build -d 
```

For Podman: 

```bash
podman-compose up --force-recreate --build -d 
```

**Important Notice:**
Depending on what you use, you have to use a specific hostname in order 
to connect to the local services inside stepzen:
- Docker: `host.docker.internal`
- Podman: `host.containers.internal`
- Alternatively: Your machine's IP address 

## Example

You can find a full example in the `example/` directory.

## Contact us

| Name| Role | Email |
| ---- |----| ----  |
| Thomas Eberle| Solution Architect | Thomas.Eberle@ibm.com |
| Stephan Orlowsky| Technology Engineer | Stephan.Orlowsky@ibm.com |
| Blandine Alazard| Technology Engineer | Blandine.Alazard@ibm.com | 
