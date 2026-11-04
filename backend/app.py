import json
import os

import boto3

def get_table():
    dynamodb = boto3.resource("dynamodb")
    table_name = os.environ["TABLE_NAME"]
    return dynamodb.Table(table_name)


def lambda_handler(event, context):
    table = get_table()

    response = table.update_item(
        Key={"id": "visitor_count"},
        UpdateExpression="ADD #count :incr",
        ExpressionAttributeNames={"#count": "count"},
        ExpressionAttributeValues={":incr": 1},
        ReturnValues="UPDATED_NEW",
    )

    count = int(response["Attributes"]["count"])

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "OPTIONS,POST",
            "Content-Type": "application/json",
        },
        "body": json.dumps({"count": count}),
    }
