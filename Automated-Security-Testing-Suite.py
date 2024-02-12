import requests
import json
import logging

logger = logging.getLogger(__name__)

class Client:
    def __init__(self, base_url):
        self.base_url = base_url
        
    def call_api(self, endpoint, params={}):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=params)
        if response.status_code != 200:
            logger.error(f"Error calling {url}")
            raise Exception(f"Error calling {url}: {response.text}")
        return response.json()

    def check_vulnerabilities(self, app_list):
        endpoints = ["vulnerability_scan"]
        results = {}
        for app in app_list:
            for endpoint in endpoints:
                try:
                    data = self.call_api(endpoint, {"app_name": app})
                    results[app] = data["results"]["critical"]
                except Exception as e:
                    logger.warning(str(e))
                    results[app] = "N/A"
        return results

client = Client("<YOUR_BASE_URL>")
apps = ["App1", "App2", "App3"]
results = client.check_vulnerabilities(apps)
print(json.dumps(results, indent=4))