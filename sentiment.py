import os, requests, uuid, json

# Don't forget to replace with your Cog Services subscription key!
subscription_key = 'xxxxxxxxxxxxxxxx'
endpoint = "xxxxxxxxxxxxxxxx"
# Our Flask route will supply four arguments: input_text, input_language,
# output_text, output_language.


def get_sentiment(input_text, input_language):
    path = '/text/analytics/v3.0/sentiment'
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = {
        'documents': [
            {
                'language': input_language,
                'id': '1',
                'text': input_text
            },
        ]
    }
    response = requests.post(constructed_url, headers=headers, json=body)
    return response.json()