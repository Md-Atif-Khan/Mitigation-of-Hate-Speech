from googleapiclient import discovery
import json

API_KEY = "your api key"

client = discovery.build(
    "commentanalyzer",
    "v1alpha1",
    developerKey=API_KEY,
    discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
    static_discovery=False,
)

analyze_request = {
    "comment": {"text": "wdcfvbgnhhvcx"},
    "requestedAttributes": {
        "TOXICITY": {},
        "SEVERE_TOXICITY": {},
        "PROFANITY": {},
        "INSULT": {},
        "IDENTITY_ATTACK": {},
        "THREAT": {}, 
    },
}

response = client.comments().analyze(body=analyze_request).execute()
# print(json.dumps(response, indent=2))

res = json.loads(json.dumps(response))
TOXICITY = res["attributeScores"]["TOXICITY"]["summaryScore"]["value"]
SEVERE_TOXICITY = res["attributeScores"]["SEVERE_TOXICITY"]["summaryScore"]["value"]
PROFANITY = res["attributeScores"]["PROFANITY"]["summaryScore"]["value"]
INSULT = res["attributeScores"]["INSULT"]["summaryScore"]["value"]
THREAT = res["attributeScores"]["THREAT"]["summaryScore"]["value"]
IDENTITY_ATTACK = res["attributeScores"]["IDENTITY_ATTACK"]["summaryScore"]["value"]

print('TOXICITY: ', TOXICITY)
print('SEVERE_TOXICITY: ', SEVERE_TOXICITY)
print('PROFANITY: ', PROFANITY)
print('INSULT: ', INSULT)
print('THREAT: ', THREAT)
print('IDENTITY_ATTACK: ', IDENTITY_ATTACK)

