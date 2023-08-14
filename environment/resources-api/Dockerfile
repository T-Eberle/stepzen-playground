
FROM golang:1.19

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY main/* resources.json ./

RUN CGO_ENABLED=0 GOOS=linux go build -o /graphql-stepzen

EXPOSE 9000

CMD ["/graphql-stepzen"]