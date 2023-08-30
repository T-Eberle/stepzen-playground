# StepZen Bootcamp: Creating queries and using fragments

In the last 5 chapters, we have focused on the setup, intialisation
and data-centered development with StepZen and GraphQL. So far, we haven't 
discussed, how to work with graphql operations / queries.

The chapter will describe the following points:

- How to query with operation files
- How to use fragments
- Generators for GraphQL clients


## Query data from GraphQL file

Graphql queries (a.k.a. operations) can be persisted 
in graphql files and can then be reused. Splitting the logic 
and queries is a good practice, as it will keep your code base clean.

Furthermore, it will save you time and complexity when developing a client,
as your queries are persisted in separate files.

A GraphQL operations file could look like this:

```graphql

query GetOrders($customerId: Int!) {
    orders($customerId: Int!) {
        order_id
        ordered_products {
            name
            description
            amount
            unit_price
            total
        }
        timestamp
        cashier_name
        payment_type
        total
    }

}

```

You can also see in this example, that it is possible to use variables such as `$customerId`.
This makes query files quite powerful, as you don't need to produce any logic 
inside your code.


## Execute GraphQL operation files by using StepZen CLI

You can also execute those files by using the stepzen CLI. 
In order to execute those queries, you have to execute the following command:

```bash
stepzen request QUERY
```

`QUERY` is in this case the path to your GraphQL file.

For more information, click on [this link](https://www.ibm.com/docs/en/stepzen?topic=reference-cli-commands#stepzen-request).

## Using fragments

Query or operation files can get quite large, if you want to return 
a lot of attributes. In many use cases, 
the same set of attributes are used for one single query, as you might
combine a subset of queries all returning the same types. This is where
fragments come into play. With fragments, it is possible to define a subset of 
attributes, which you then can use in your queries to save lines of code.

Let's assume the following operation file:

```graphql
query getPets{
    cats {
        name
        gender
        age
        race
        is_good
        catches_mice
        vomits_hairballs
    }

    dogs {
        name
        gender
        age
        race
        is_good
        catches_cats
    }
}
```

As you can see in this example, we are using a few same attributes for both 
queries `cats` and `dogs`.

We assume that the graphQL types `Cat` and `Dog` implement both the interface `Pet`.

By using fragments you can combine the similar attributes like this:

```graphql
fragment PetAttributes on Pet {
    name
    gender
    age
    race
    is_good
}

query getPets{
    cats {
        ...PetAttributes
        catches_mice
        vomits_hairballs
    }

    dogs {
        ...PetAttributes
        catches_cats
    }
}
```

Fragments are therefore a great way to keep your query files tidy.

## Using generators to generate code for GraphQL clients

There is an excellent code generator you can find [here](https://the-guild.dev/graphql/codegen).

With this code generator, you can generate everything required for your client 
beginning from schema types and ending with operations. This is an useful 
addition for StepZen, as you can create server by deploying server and generate 
your client by using the code generator.


