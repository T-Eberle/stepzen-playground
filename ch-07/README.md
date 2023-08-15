# StepZen Bootcamp: Mocking and Testing

## Mock data with StepZen

With StepZen, it is possible to mock data to replace data resources, 
especially if the data source is currently not available or generated.

This can be used to prepare your graphql schema files and test them, 
before actually having data sources available.

For more information click [here](https://www.ibm.com/docs/en/stepzen?topic=reference-use-mock-data#the--mock-directive).

## Testing with VS Code

For testing in VS Code, we recommend using the extension 
[Rest Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).
With this extension, you can create `.http` files with prepared requests and 
execute them. In the `example/test` directory, 
you can see multiple examples of tests: You can send standard Graphql queries 
to your local StepZen dev environment.

Important Notice: In order to execute the requests, 
you have to change `#YOUR_API_KEY` to your API key. 
You can get your local API key when you execute the following command: 

```bash
stepzen whoami --apikey
```
