package main

import (
	"github.com/graphql-go/graphql"
	"golang.org/x/exp/slices"
)

var resourceType = graphql.NewObject(graphql.ObjectConfig{
	Name: "Resource",
	Fields: graphql.Fields{
		"id": &graphql.Field{
			Type: graphql.Int,
		},
		"name": &graphql.Field{
			Type: graphql.String,
		},
		"provider": &graphql.Field{
			Type: graphql.String,
		},
		"type": &graphql.Field{
			Type: graphql.String,
		},

		"created": &graphql.Field{
			Type: graphql.DateTime,
		},
		"updated": &graphql.Field{
			Type: graphql.DateTime,
		},
		"cpu_util": &graphql.Field{
			Type: graphql.Float,
		},
		"mem_util": &graphql.Field{
			Type: graphql.Float,
		},
		"total_space_gb": &graphql.Field{
			Type: graphql.Int,
		},
		"free_space_gb": &graphql.Field{
			Type: graphql.Float,
		},
	},
})

var ResourceList []Resource
var _ = importJSONDataFromFile("./resources.json", &ResourceList)

var rootQuery = graphql.NewObject(graphql.ObjectConfig{
	Name: "ResourceQueries",
	Fields: graphql.Fields{
		"resourceById": &graphql.Field{
			Type:        resourceType,
			Description: "Get resource by id.",
			Args: graphql.FieldConfigArgument{
				"id": &graphql.ArgumentConfig{
					Type: graphql.Int,
				},
			},
			Resolve: func(params graphql.ResolveParams) (interface{}, error) {

				idQuery, isOk := params.Args["id"].(int)
				if isOk {
					for _, resource := range ResourceList {
						if resource.ID == idQuery {
							return resource, nil
						}
					}
				}
				return Resource{}, nil
			},
		},
		"resourceFilterByIds": &graphql.Field{
			Type:        graphql.NewList(resourceType),
			Description: "List resources matching IDs.",
			Args: graphql.FieldConfigArgument{
				"ids": &graphql.ArgumentConfig{
					Type: graphql.NewList(graphql.Int),
				},
			},
			Resolve: func(params graphql.ResolveParams) (interface{}, error) {
				idQueryInterface, isOk := params.Args["ids"].([]interface{})
				idQuery := make([]int, 0, len(idQueryInterface))
				for _, v := range idQueryInterface {
					idQuery = append(idQuery, v.(int))
				}

				if isOk {
					var resources []Resource
					for _, resource := range ResourceList {

						if slices.Contains(idQuery, resource.ID) {
							resources = append(resources, resource)
						}
					}
					return resources, nil
				}
				return []Resource{}, nil
			},
		},
		"resourcesList": &graphql.Field{
			Type:        graphql.NewList(resourceType),
			Description: "Returns all resources",
			Resolve: func(p graphql.ResolveParams) (interface{}, error) {
				return ResourceList, nil
			},
		},
	},
})

var ResourceSchema, _ = graphql.NewSchema(
	graphql.SchemaConfig{
		Query: rootQuery,
	},
)
