from app import connex_app
import pytest
import requests

# get the url of api
url = 'http://127.0.0.1:5000/api/people'
# test api with status
def test_api():
    r = requests.get(url)
    assert r.status_code == 200

#
def test_people_api_name():
    response = requests.get(url)
    response_body = response.json()
    assert response_body[::][0]['fname'] == 'prasad'


