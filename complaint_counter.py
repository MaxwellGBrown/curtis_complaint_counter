"""An AWS Lambda endpoint expecting Slack integration requests."""
import time
import urllib.parse
import uuid

try:
    from boto3 import client
except ModuleNotFoundError:
    # Probably testing. Fuck it.
    from unittest.mock import Mock
    client = Mock()


dynamodb = client('dynamodb')


def lambda_handler(event, context=None):
    """Lamdba endpoint to count curtis's complaints."""
    parsed_body = urllib.parse.parse_qs(event["body"])
    # query strings can be multiple; just take the first of each found
    request_body = {k: v[0] for k, v in parsed_body.items()}

    command_text = request_body.get('text', '')

    # Store complaint in data store
    dynamodb.put_item(
        TableName="CurtisComplaints",
        Item={
            "uuid": {"S": str(uuid.uuid4())},
            "timestamp": {"N": f"{time.time():.10g}"},
            "complaint": {"S": command_text},
            "reporter": {"S": request_body['user_name']},
        }
    )

    response_body = f'*Curtis Complained!*\n\n> {command_text}'

    # NOTE: scanning a dynamo table can be a really expensive operation, but
    #       it's the only way to get a live count of records in the table.
    #       Since this table will likely only be very small it will likely be
    #       okay for the forseeable future.
    scan = dynamodb.scan(TableName="CurtisComplaints")
    response_body += f'\n\nCurtis has *{scan["Count"]}* recorded complaints.'

    response = {
        'statusCode': 200,
        'headers': dict(),
        'body': response_body,
    }
    return response
