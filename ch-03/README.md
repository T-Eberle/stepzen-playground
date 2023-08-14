# StepZen Bootcamp: Generate and Connect

## Syntax of a graphql file

For more information about the graphql syntax, click [here](https://graphql.org/learn/schema/).

### Import via Stepzen cli

To import a data source via the StepZen CLI, you run the `stepzen import` 
command. Depending on your data source, you set the right argument and the 
necessary URL.

To import e.g. a REST API, you run the following command: 

```bash
stepzen import curl https://introspection.apis.stepzen.com/customers --query-name "customers" --query-type "Customer" --name "customers"
```

With the option `query-name` you set the name of the query, which will be 
created behind this REST request. The option `query-type` defines the graphql 
type, which is supposed to be returned by the REST request as a response.

For more details, click [here](https://www.ibm.com/docs/en/stepzen?topic=quickstart-transform-rest-graphql).

### Create graphql file manually

Besides the ability to generate graphql schemes depending on your data sources 
and the command `stepzen import`, there are several reasons why you would 
consider to create the scheme files by your own. It will give you more 
flexibility in your structure of defining the graphql schemes. Especially when y
ou start combining data sources in one dataset, you will have to do manual changes.

## Deploy a graphql scheme file

To deploy a StepZen API via the CLI, consider the following steps:

1. You need to be logged in on your local or cloud-based StepZen instance and 
account. This can be done via the command `stepzen login`. See also 
[here](https://www.ibm.com/docs/en/stepzen?topic=reference-cli-commands#stepzen-login). 
For connecting to a local docker environment, check this link [here](https://www.ibm.com/docs/en/stepzen?topic=apis-local-development-in-docker)
2.  When you are logged in successfully, you can deploy your graphql project 
to your public StepZen account with the command `stepzen deploy`. See also [here](https://www.ibm.com/docs/en/stepzen?topic=reference-cli-commands#stepzen-deploy).

Important Note: When you deploy your API (step 2), you need to be in the 
project directory with the current session of your terminal.
Furthermore, you should have a similar project structure as described in 
chapter 
[StepZen project structure](../ch-02/README.md#stepzen-project-structure) - 
you will at least require an `index.grapqhl` and the `stepzen.config.json` file 
in the root path of your project directory.

## Exercises

### Task 1

Import the `resources-api` with the `stepzen import` command. All your types 
and queries should be inside the `resources` folder.

**URL for Podman:** *http://host.containers.internal:19000/graphql*

**URL for Docker:** *http://host.docker.internal:19000/graphql*

<details>
<summary><b>Results</b></summary>
To import the `resources-api`, simply execute the following command (for podman):

```bash
stepzen import graphql http://host.containers.internal:19000/graphql --name=resources
```

</details>

### Task 2

Import the MySQL(MariaDB) database `sust-db` via `stepzen import`.

Information about the database:

**Host:** *host.containers.internal:3306* / *host.docker.internal:3306*

**Username:** *user*

**Password:** *password*

**Database:** *db*

<details>
<summary><b>Results</b></summary>
To import the `sust-db`, execute the following command:

```bash
stepzen import mysql mysql://user.password@host.containers.internal:3306/db --name=sust-db
```

</details>

### Task 3

Import the PostgreSQL database `cost-db` via `stepzen import`

**Host:** *host.containers.internal:15432* / *host.docker.internal:15432*

**Username:** *user*

**Password:** *password*

**Database:** *cost*

<details>
<summary><b>Results</b></summary>
To import the `cost-db` via `stepzen import`, execute the following command:

```bash
stepzen import postgresql postgresql://host.containers.internal:15432/cost?user=user&password=password
```

</details>
