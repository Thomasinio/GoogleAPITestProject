from tests.api import api_client
from src.test_data import TestData


get_event_endpoint = "calendar/v3/calendars/{}/events/{}"
quick_add_event_endpoint = "calendar/v3/calendars/{}/events/quickAdd"


def test_add_event(calendar_fixture):

    access_token = calendar_fixture

    random_event_name = TestData().text_generator()
    r = api_client.post(quick_add_event_endpoint.format(TestData.test_user.email),
                        headers={"Authorization": access_token},
                        params={"text": random_event_name})
    r = api_client.get(get_event_endpoint.format(TestData.test_user.email, r.json()["id"]),
                       headers={"Authorization": access_token})
    assert r.json()["summary"] == random_event_name


def test_add_event_duplicate(calendar_fixture):

    access_token = calendar_fixture

    random_event_name = TestData().text_generator()
    r1 = api_client.post(quick_add_event_endpoint.format(TestData.test_user.email),
                        headers={"Authorization": access_token},
                        params={"text": random_event_name})
    r2 = api_client.post(quick_add_event_endpoint.format(TestData.test_user.email),
                        headers={"Authorization": access_token},
                        params={"text": random_event_name})
    r1 = api_client.get(get_event_endpoint.format(TestData.test_user.email, r1.json()["id"]),
                       headers={"Authorization": access_token})
    r2 = api_client.get(get_event_endpoint.format(TestData.test_user.email, r2.json()["id"]),
                       headers={"Authorization": access_token})
    assert r1.json()["summary"] == random_event_name
    assert r2.json()["summary"] == random_event_name
    assert r1.json()["id"] != r2.json()["id"]


def test_add_event_empty_name(calendar_fixture):

    access_token = calendar_fixture

    r = api_client.post(quick_add_event_endpoint.format(TestData.test_user.email),
                        headers={"Authorization": access_token},
                        params={"text": ""})

    r = api_client.get(get_event_endpoint.format(TestData.test_user.email, r.json()["id"]),
                       headers={"Authorization": access_token})

    assert "summary" not in r.json()
    assert r.json()["status"] == "confirmed"


def test_add_event_no_name(calendar_fixture):

    access_token = calendar_fixture

    r = api_client.post(quick_add_event_endpoint.format(TestData.test_user.email),
                        headers={"Authorization": access_token},
                        raise_for_status=False)

    assert r.status_code == 400
    assert r.json()["error"]["message"] == "Required parameter: text"


def test_add_event_invalid_auth(calendar_fixture):

    access_token = calendar_fixture

    random_event_name = TestData().text_generator()
    r = api_client.post(quick_add_event_endpoint.format(TestData.test_user.email),
                        headers={"Authorization": access_token + "1"},
                        params={"text": random_event_name},
                        raise_for_status=False)

    assert r.status_code == 401
    assert r.json()["error"]["message"] == "Invalid Credentials"
