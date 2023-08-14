# StepZen Bootcamp: Extend

## Extend your types with `extend`

When using `@materializer`, it is possible to *extend* a basic type to add more attributes.
With extend, you can organise your data structure better and you are able to 
update your base types and its attributes.

Let's assume we have a `Customer`, which keeps the basic data of this type:

```graphql
type Customer {
    id: Int!
    name: String!
    street: String
    streetNumber: String
    postalCode: String!
    city: String!
    country: String
}
```

If - for example - I want to add a `Wallet` with a separate type to each of my 
customer, I can do this by **extending** my basic `Customer` type:

```graphql
extend type Customer{
    wallet: Wallet
    @materializer(
        query: "walletByCustomerId"
        arguments: [{ name: "id", field: "customer_id" }]
    )
}
```

Without even touching the base type, I was able to extend my `Customer` type 
with extra attributes.

## Define an abstract type layer with `interface`

With `interfaces` I am able to define an abstract layer on top of my types. 
This is technically similar to an `extend`. 
However, the main purpose of interfaces is inheritence and not extending base types.

In StepZen, interfaces can be used to combine the types in single queries. 
This means that a frontend developer can use the interface queries to request 
data from different types and queries, which implement this interface.

For more information on the usage of interfaces to access multiple backends,
 click [here](https://www.ibm.com/docs/en/stepzen?topic=schemas-use-interfaces-access-multiple-backends).

## Exercises

### Task 1

Create an interface `Capability` with the following attributes:

- `name` of type `String`, required
- `description` of type `String`, optional
- `resource_id` of type `Int`, optional
- `resource` of type `Resource`, optional

Let the types `Sustainability` and `Cost` implement from this interface.

Furthermore, create a query `capabilitiesById` to list all available 
capabilities of a resource. and connect your queries from the implementing 
types `Cost` and `Sustainability` with the interface query.
As soon as you finished the task, test and execute the query in your local 
StepZen instance.


<details>
<summary><b>Results</b></summary>

Create the following interface and its query:

```graphql
interface Capability {
    name: String!
    resource_id: Int
    description: String
    resource: Int
}

type Query {
    capabilitiesById(resource_id: )
}
```

</details>
