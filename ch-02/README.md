# StepZen Bootcamp: Create and Prepare

## Initialise a StepZen project

To initialise a stepzen project / workspace, enter the following command:

```bash
stepzen init
```

This will guide you through a prompt dialog, 
where you have to define a name/path for your api.

After this, you will have a `stepzen.config.json` file inside your workspace, 
including the defined name of your api.

## StepZen project structure

```bash
.
├── stepzen.config.json
├── README.md
├── nested_schema_file
│   └── schema_a.graphql
├── another_nested_schema_file
│   └── schema_b.graphql
├── config.yaml
└── index.graphql
```

The `stepzen.config.json` keeps all information of the api project 
wide configuration concerning StepZen. 

In the root directory, StepZen expects an `index.graphql` file. 
This can either define all schemes and queries or it can reference other files
in this project directory. It is recommended to split the logic of the StepZen
API into separate graphql files and combine them with the root `index.grapqhl` 
file.

In this example, the `index.graphql` could look like this:

```grapqhl

schema
  @sdl(
    files: [
      "nested_schema_file/schema_a.graphql"
      "another_nested_schema_file/schema_b.graphql"
    ]
  ) {
  query: Query
}
```

In case you want to add other graphql files, you simply add them to the root 
`index.graphql` file.

## Exercises

### Task 1

Create a new StepZen project with `stepzen init`. Call your api `api/bootcamp`.

<details>
<summary><b>Results</b></summary>
To generate a new StepZen project with the `stepzen init` command, run the 
following command in your desired target directory for this project: 

```bash
stepzen init
```

For more information, click [here](https://www.ibm.com/docs/en/stepzen?topic=reference-cli-commands#stepzen-init).
</details>


