import os
import json

project_path = os.path.dirname(os.path.abspath(__file__))

try:
    with open(os.path.join(project_path, "config.json"), "r") as f:
        config = json.load(f)
except FileNotFoundError as e:
    raise e

base_url = config["base_url"]
access_token = config["access_token"]
