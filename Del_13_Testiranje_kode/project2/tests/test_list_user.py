import pytest
import requests
import json


def test_list_invaliduser(supply_url):
    url = supply_url + "/users/50"
    resp = requests.get(url)
    assert resp.status_code == 404, resp.text
