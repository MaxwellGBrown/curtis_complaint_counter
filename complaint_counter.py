"""An AWS Lambda endpoint expecting Slack integration requests."""


def lambda_handler(event, context=None):
    """Lamdba endpoint to count curtis's complaints."""
    response = {
        'statusCode': 200,
        'headers': dict(),
        'body': '',
    }
    return response
