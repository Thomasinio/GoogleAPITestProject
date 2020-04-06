import requests
from urllib.parse import urljoin
from config_loader import base_url


class APIClient:
    """Simplified client for working with the API"""

    def get(self, path="/", params=None, headers=None, json=None):

        url = urljoin(base_url, path)
        r = requests.get(url, params=params, headers=headers, json=json)
        r.raise_for_status()
        return r

    def post(self, path="/", params=None, headers=None, data=None, json=None, files=None, raise_for_status=True):

        url = urljoin(base_url, path)
        r = requests.post(url, params=params, headers=headers, data=data, json=json, files=files)
        if raise_for_status:
            r.raise_for_status()
        return r

    def put(self, path="/", params=None, headers=None, json=None):

        url = urljoin(base_url, path)
        r = requests.put(url, params=params, headers=headers, json=json)
        r.raise_for_status()
        return r

    def delete(self, path="/", headers=None):

        url = urljoin(base_url, path)
        r = requests.delete(url, headers=headers)
        r.raise_for_status()
        return r
