from googleapiclient import discovery
import requests
import json

def getBook():
  payload = {"id":"49552", "format":"json", "key":"HS66eaLfPB08Hj6xsMXR1w"}

  result = requests.get("https://www.goodreads.com/book/show", params=payload)
  print(result.text)
  

API_KEY='AIzaSyCz6SB8wHrLTskOpCKSbmx-pWTKiy5XLX0'

# Generates API client object dynamically based on service name and version.
service = discovery.build('commentanalyzer', 'v1alpha1', developerKey=API_KEY)

analyze_request = {
  'comment': { 'text': 'friendly greetings from python you fucker' },
  'requestedAttributes': {'TOXICITY': {}}
}

response = service.comments().analyze(body=analyze_request).execute()

print json.dumps(response, indent=2)

getBook()
