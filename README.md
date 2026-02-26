# severless-task-tracker
Small project on using AWS tools to create and use simple tasks

#the specifics of what it does:
- User can create a task with a title and its priority.
- Stores the tasks in a DynamoDB table inside AWS.
- Lets the user lists all their stored tasks.

## Involved AWS services 

- **Lambda** - this runs code when a user calls the API.
- **API Gateway** - receive and send HTTP requests to Lambda.
- ** DynamoDB** - NoSQL database which stores the task
- **IAM** - controls the user and services access to the API and database

## Language

- Python (code for Lambda function)
