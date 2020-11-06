import requests
from requests.exceptions import HTTPError, Timeout, ConnectionError


def get_api_data(url: str, params: dict = None, headers: dict = None, timeout: int = 3):
    """
    Make a request to specified URL. If not found return None.
    """
    try:
        response = requests.get(url, params=params, headers=headers, timeout=timeout)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occured: {http_err}.")
    except ConnectionError as conn_err:
        print(f"Network problem occured: {conn_err}")
    except Timeout as time_err:
        print(f"Timeout! : {time_err}")
    except Exception as err:
        print(err)
    else:
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Wrong response code: {response.status_code}")
            return None


if __name__ == "__main__":
    url_users = "https://jsonplaceholder.typicode.com/users"
    data = get_api_data(url_users, params={"id": 8})
    if data:
        print(data[0])
    else:
        print("Ni podatkov")
