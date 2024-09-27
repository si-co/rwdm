import requests
import json

# Elasticsearch endpoint of entscheidsuche.ch
url = "https://entscheidsuche.pansoft.de:9200/entscheidsuche-*/_search"

# Elasticsearch query to be sent
search_query = {
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "attachment.content": "WhatsApp"
                    }
                }
            ],
            "should": [
                {
                    "match_phrase": {
                        "attachment.content": "droit pénal"
                    }
                },
                {
                    "match_phrase": {
                        "attachment.content": "chambre pénale"
                    }
                },
                {
                    "match_phrase": {
                        "attachment.content": "diritto penale"
                    }
                }
            ],
            "minimum_should_match": 1
        }
    },
    "size": 10000  # Size parameter inside the body as per the guide
}

# Headers
headers = {
    "Content-Type": "application/json"
}

# Send the request directly using requests library
response = requests.post(url, headers=headers, data=json.dumps(search_query))

# Check if the request was successful
if response.status_code == 200:
    # Parse and print the results
    results = response.json()
    for hit in results['hits']['hits']:
        if hit['_source']['attachment']['language'] != 'de':
            print(hit['_source']['attachment']['content_url'])
else:
    print(f"Error: {response.status_code} - {response.text}")

