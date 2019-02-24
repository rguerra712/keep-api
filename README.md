# Serverless Keep API
An unofficial serverless-hosted solution for the keep api built around the use of the [gkeepapi](https://github.com/kiwiz/gkeepapi) project.

# To deploy
1. Clone this repository
1. Deploy it using the `serverless deploy` command

# Usage
Upon deploying the API using the steps above, you can then:
* GET all notes by navigating to the output API above at `https://<UNIQUE_ID>.execute-api.us-east-1.amazonaws.com/dev/notes?email=<YOUR_USERNAME>&password==<YOUR_PASSWORD>`
* POST a new note by posting to the API above at `https://<UNIQUE_ID>.execute-api.us-east-1.amazonaws.com/dev/notes?email=<YOUR_USERNAME>&password==<YOUR_PASSWORD>` with a body of the form:
```
{
  "title": "<YOUR TITLE HERE>",
  "text": "<YOUR TEXT HERE>"
}
```
