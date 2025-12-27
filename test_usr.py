import requests

url = "http://127.0.0.1:8000/polaris/usr"
headers = {"Content-Type": "text/xml"}
body = """<call model="LAV:J:A:A:2024031900" srcid="00000000000000000000"><usr method="get"/></call>"""

try:
    print(f"Sending POST to {url}...")
    response = requests.post(url, data=body, headers=headers)
    print(f"Status Code: {response.status_code}")
    print("Response Body:")
    print(response.text[:500]) # Print first 500 chars
except Exception as e:
    print(f"Error: {e}")
