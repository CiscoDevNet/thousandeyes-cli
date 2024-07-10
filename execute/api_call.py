import requests
from typing import Optional, Union, Dict, Any


def api_get_data(token: str, resource: str, aid: Optional[str] = None) -> Union[str, Dict[str, Any]]:
    """
    Fetch data from the ThousandEyes API.

    Args:
        token (str): API authentication token.
        resource (str): API resource to fetch.
        aid (Optional[str]): Account ID, if applicable.

    Returns:
        Union[str, Dict[str, Any]]: JSON response or error message.
    """
    url = f"https://api.thousandeyes.com/v7/{resource}"
    if aid:
        url += f"?aid={aid}"

    headers = {
        "content-type": "application/json",
        "Authorization": f"Bearer {token}",
    }

    try:
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        error_messages = {
            401: "Error: Unauthorized. Check your credentials.",
            403: "Error: Forbidden. You don't have the necessary permissions.",
            404: f"Error: Not Found. The resource {resource} was not found.",
            429: "Error: Too Many Requests. You've hit the rate limit.",
        }
        return error_messages.get(response.status_code, f"An HTTP Error occurred: {http_err}")
    except Exception as err:
        return f"An Error occurred: {err}"