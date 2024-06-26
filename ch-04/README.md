# StepZen Bootcamp: Combine and Transform


## Use @materializer

By using the `@materializer`, it is possible to build a "graph of graphs". 
This means that you can integrate data sources to other data sources by just 
defining a graphql schema. This is one of the top features of StepZen 
and gives developers the ability to easily extend their graphql types.

A full example with `Customers` and `Orders` can be found 
[here](https://www.ibm.com/docs/en/stepzen?topic=schemas-link-types-materializer#combine-subgraphs-using-the-materializer-directive). 
More information about extending types can be found [in the next chapter](../ch-05/README.md).

## Transform

Sometimes it is necessary to transform attributes or objects to a different 
structure for your REST APIs: Especially if you have a defined data structure 
for different datasources.

As soon as you will start to use interfaces,
you will probably use several transforms for your APIs in order to set the 
right attribute names.
There are different types of transforms, which you can find [here](https://www.ibm.com/docs/en/stepzen?topic=reference-directives#transforms).

## Exercises

### Task 1

By using the `@materializer`, extend the `Cost` type and add a 
`resource` attribute with the type `Resource`. 

<details>
<summary><b>Results</b></summary>

In your  `cost-db/index.graphql` file, add the following extension: 

```graphql
extend type cost {
  resource: Resource
    @materializer(
      query: "resourceById"
      arguments: [{ name: "id", field: "resource_id" }]
    )
}
```

</details>

### Task 2

By using the `@materializer`, extend the `Sustainability` type and add a 
`resource` attribute with the type `Resource`. 

<details>
<summary><b>Results</b></summary>

In your  `sust-db/index.graphql` file, add the following extension: 

```graphql
extend type sustainability {
  resources: Resource
    @materializer(
      query: "resourceById"
      arguments: [{ name: "id", field: "resource_id" }]
    )
}
```

</details>

### Task 3

By using the `@materializer`, extend the `Project` type and add a 
`resources` attribute with the type `[Resource]`.

<details>
<summary><b>Results</b></summary>


In your  `agile-api/index.graphql` file, add the following extension: 

```graphql
extend type project {
  resources: [Resource]
  @materializer(
      query: "resourceFilterByIds"
      arguments: [{ name: "ids", field: "resource_ids" }]
    )
}
```

</details>

### Task 4

Import the agile-api manually by creating a graphql file.

Type: 

```graphql
type project {
  agile_method: String
  description: String
  id: Int
  is_completed: Boolean
  name: String
  resource_ids: [Int]
  team_members_amount: Int
}
```

Queries:
- `http://host.containers.internal:18080/api/projects/$id` -> Returns a single project by id
- `http://host.containers.internal:18080/api/projects/` -> Returns all projects as an array

Extend:
Resource type by using the resource_ids (plural!)


<details>
<summary><b>Results</b></summary>

A sample solution could look like this:

```graphql
type project {
  agile_method: String
  description: String
  id: Int
  is_completed: Boolean
  name: String
  resource_ids: [Int]
  team_members_amount: Int
}

extend type project {
  resources: [Resource]
    @materializer(
      query: "resourceFilterByIds"
      arguments: [{ name: "ids", field: "resource_ids" }]
    )
}

type Query {
  projectsList: [project]
    @rest(
      endpoint: "http://$url/api/projects/"
      configuration: "agile-api-config"
      transforms: [
        {
          pathpattern: []
          editor: """
          jq: .projects[]
          """
        }
      ]
    )
  projectById(id: String!): project
    @rest(
      endpoint: "http://$url/api/projects/$id"
      configuration: "agile-api-config"
    )
}
```

</details>

### Task 5

For the Projects/Agile graphql type and the `projectsList`-Query, flatten the 
array by using `jq` (Flatten => Turn the `projects`- array inside 
the response to the root array.)

<details>
<summary><b>Results</b></summary>

For this, you need to 

```graphql
projectsList: [project]
    @rest(
      endpoint: "http://$url/api/projects/"
      configuration: "agile-api-config"
      transforms: [
        {
          pathpattern: []
          editor: """
          jq: .projects[]
          """
        }
      ]
    )

```

</details>

