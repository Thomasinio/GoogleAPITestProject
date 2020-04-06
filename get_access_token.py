import json

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


def main():
    """Get access token and add this value into the configuration file for test executions"""
    SCOPES = "https://www.googleapis.com/auth/calendar"
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
        build('calendar', 'v3', http=creds.authorize(Http()))

    try:
        config_file = open("config.json", "r")
    except FileNotFoundError as e:
        raise e
    json_object = json.load(config_file)
    config_file.close()

    json_object["access_token"] = creds.access_token

    config_file = open("config.json", "w")
    json.dump(json_object, config_file)
    config_file.close()


if __name__ == "__main__":
    main()
