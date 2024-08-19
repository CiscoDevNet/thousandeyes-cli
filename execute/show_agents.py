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

from typing import Optional

from .execute_commands import ShowCommand


def show_agents(
    token: str,
    file_format: str,
    aid: Optional[str] = None,
    write: bool = False
) -> str:
    """
    Fetch and format agent information.

    Args:
        token (str): The authentication token for API calls.
        file_format (str): The desired output format (json, yaml, csv, human).
        aid (Optional[str]): The account ID, if applicable. Defaults to None.
        write (bool): Whether to write the output to a file. Defaults to False.

    Returns:
        str: Formatted agent information or a message indicating file creation.
    """
    show_command = ShowCommand(token)
    return show_command("agents", file_format, aid, write)
