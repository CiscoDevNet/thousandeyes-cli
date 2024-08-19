# Copyright 2024 Cisco Systems, Inc. and its affiliates
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

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
            401: "Error: Invalid Token. Check your Bearer Token.",
            403: "Error: Forbidden. You don't have the necessary permissions.",
            404: f"Error: Not Found. The resource {resource} was not found.",
            429: "Error: Too Many Requests. You've hit the rate limit.",
        }
        return error_messages.get(response.status_code, f"An HTTP Error occurred: {http_err}")
    except Exception as err:
        return f"An Error occurred: {err}"
