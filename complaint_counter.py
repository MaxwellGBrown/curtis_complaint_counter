"""An AWS Lambda endpoint expecting Slack integration requests."""
import urllib.parse


def lambda_handler(event, context=None):
    """Lamdba endpoint to count curtis's complaints."""
    request_body = urllib.parse.parse_qs(event['body'])

    # for some reason text comes out as a string in a list
    command_text = request_body.get('text', [''])[0]

    response_body = f'Curtis Complained!\n\n> {command_text}'

    response = {
        'statusCode': 200,
        'headers': dict(),
        'body': response_body,
    }
    return response
