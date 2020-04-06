from config_loader import access_token


def get_authorization():
    return "Bearer " + access_token
