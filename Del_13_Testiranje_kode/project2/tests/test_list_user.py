import pytest
import requests
import json


@pytest.mark.parametrize("user_id, firstname", [(1, "George"), (2, "Janet")])
def test_list_valid_user(supply_url, user_id, firstname):
    url = supply_url + f"/users/{user_id}"
    resp = requests.get(url)
    j = json.loads(resp.text)
    assert resp.status_code == 200
    assert j["data"]["id"] == user_id
    assert j["data"]["first_name"] == firstname


def test_list_invaliduser(supply_url):
    url = supply_url + "/users/50"
    resp = requests.get(url)
    assert resp.status_code == 404, resp.text
