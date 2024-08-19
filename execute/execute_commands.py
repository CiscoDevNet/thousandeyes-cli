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

import yaml
import json
from datetime import datetime
from pathlib import Path
from typing import Optional

from jinja2 import Environment, FileSystemLoader

from .api_call import api_get_data  # Assuming api_get_data is defined in api_call.py


class ShowCommand:
    """A class to handle show commands and format output."""

    def __init__(self, token: str):
        """
        Initialize the ShowCommand class.

        Args:
            token (str): The authentication token for API calls.
        """
        self.token = token
        self.env = Environment(loader=FileSystemLoader("./templates"))

    def __call__(
        self,
        resource: str,
        file_format: str,
        aid: Optional[str] = None,
        write: bool = False,
    ) -> str:
        """
        Execute the show command.

        Args:
            resource (str): The API resource to fetch.
            file_format (str): The desired output format (json, yaml, csv, human).
            aid (Optional[str]): The account ID, if applicable.
            write (bool): Whether to write the output to a file.

        Returns:
            str: The formatted output or a message indicating file creation.
        """
        data = api_get_data(self.token, resource, aid)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        if file_format == "json":
            output = json.dumps(data, indent=4)
        elif file_format in ["yaml", "csv", "human"]:
            if file_format == "yaml":
                output = yaml.dump(data)
            else:
                resource_file = resource.replace("/", "_").replace("-", "_")
                template = self.env.get_template(f"{resource_file}_{file_format}.j2")
                output = template.render(data=data)
        else:
            return "Error: Invalid format specified"

        if write:
            return self._write_to_file(resource, timestamp, file_format, output)
        return output

    def _write_to_file(
        self, resource: str, timestamp: str, file_format: str, content: str
    ) -> str:
        """
        Write the output to a file.

        Args:
            resource (str): The API resource name.
            timestamp (str): The timestamp for the file name.
            file_format (str): The file format.
            content (str): The content to write.

        Returns:
            str: A message indicating the file creation.
        """
        resource_file = resource.replace("/", "_").replace("-", "_")
        output_dir = Path("./output")
        output_dir.mkdir(exist_ok=True)
        
        file_path = output_dir / f"{resource_file}_{timestamp}.{file_format}"
        file_path.write_text(content)
        
        return f"File created: {file_path}"
