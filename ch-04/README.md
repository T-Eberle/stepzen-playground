# StepZen Bootcamp: Combine and Transform


## Use @materializer

By using the `@materializer`, it is possible to build a "graph of graphs". 
This means that you can integrate data sources to other data sources by just 
defining a graphql schema. This is one of the top features of StepZen 
and gives developers the ability to easily extend their graphql types.

A full example with `Customers` and `Orders` can be found [here](https://stepzen.com/docs/connecting-backends/stitching). 
More information about extending types can be found [in the next chapter](../ch-05/README.md).

## Transform

Sometimes it is necessary to transform attributes or objects to a different 
structure for your REST APIs: Especially if you have a defined data structure 
for different datasources.

As soon as you will start to use interfaces,
you will probably use several transforms for your APIs in order to set the 
right attribute names.
There are different types of transforms, which you can find [here](https://stepzen.com/docs/custom-graphql-directives/directives#transforms).

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

For the Projects/Agile graphql type, transform the nested `projects`-array to an
unnested array.

<details>
<summary><b>Results</b></summary>
</details>

