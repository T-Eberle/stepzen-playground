package main

import (
	"github.com/graphql-go/handler"
	"net/http"
)

func main() {
	h := handler.New(&handler.Config{
		Schema:   &ResourceSchema,
		Pretty:   true,
		GraphiQL: true,
	})
	http.Handle("/graphql", h)
	var _ = http.ListenAndServe(":9000", nil)
}
