import json
import os
import boto3
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
TABLE_NAME = os.environ.get("TASK_TABLE_NAME", "Tasks")

table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    """
    Simple Lambda handler for the serverless-task-tracker.

    - If HTTP method is POST: create a new task.
    - If HTTP method is GET: return all tasks.
    """

    http_method = event.get("httpMethod", "GET")

    if http_method == "POST":
        body = json.loads(event.get("body", "{}"))
        title = body.get("title")
        priority = body.get("priority", "normal")

        if not title:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "title is required"})
            }

        item = {
            "id": datetime.utcnow().isoformat(),
            "title": title,
            "priority": priority,
        }

        table.put_item(Item=item)

        return {
            "statusCode": 201,
            "body": json.dumps({"message": "task created", "task": item})
        }

    # default: list tasks
    response = table.scan()
    tasks = response.get("Items", [])

    return {
        "statusCode": 200,
        "body": json.dumps({"tasks": tasks})
    }
