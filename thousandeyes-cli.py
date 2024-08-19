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

import os
import re
import socket
from getpass import getpass
import importlib
from typing import Tuple, Optional, Dict, List
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# Constants
EXECUTE_DIRECTORY = "./execute"
OUTPUT_DIRECTORY = "./output"
API_HOST = "api.thousandeyes.com"
HISTORY_FILE = "history.txt"

console = Console()

def parse_command(command_str: str) -> Tuple[Optional[str], str, Optional[str], bool]:
    """Parse the command string into its components."""
    resource = re.search(r"show\s+(.*?)(?=\s+write|\s+aid|\s+file|$)", command_str)
    file_format = re.search(r"file\s+(yaml|csv|json|human)", command_str)
    aid = re.search(r"aid\s+(\d+)", command_str)
    return (
        resource.group(1).strip() if resource else None,
        file_format.group(1) if file_format else "json",
        aid.group(1) if aid else None,
        "write" in command_str,
    )

def get_show_commands() -> Dict[str, str]:
    """Get available show commands from the execute directory."""
    return {
        file.replace("show_", "").replace(".py", "").replace("_", " "): f"execute.{file.replace('.py', '')}"
        for file in os.listdir(EXECUTE_DIRECTORY)
        if file.startswith("show_") and file.endswith(".py")
    }

def execute_show_resources() -> List[str]:
    """Get a sorted list of available show resources."""
    return sorted(get_show_commands().keys())

def check_api_status() -> str:
    """Check the ThousandEyes API status."""
    try:
        socket.gethostbyname(API_HOST)
        return "Accessible"
    except socket.gaierror:
        return "Not accessible"

def execute_show_command(
    resource: str,
    token: str,
    file_format: str,
    aid: Optional[str],
    write: bool,
    debug_enabled: bool
) -> None:
    """Execute a show command and print the output."""
    show_commands = get_show_commands()
    if resource in show_commands:
        module = importlib.import_module(show_commands[resource])
        function_name = f"show_{resource.replace(' ', '_')}"
        function = getattr(module, function_name, None)
        if function:
            output = function(token, file_format, aid, write)
            if "Error" in output:
                console.print(output.replace('"', ""), style="bold red")
            else:
                console.print(output)
            if debug_enabled:
                console.print(f"{resource=} {file_format=}, {aid=} {write=}")
        else:
            console.print(f"Function {function_name} not found in module {show_commands[resource]}", style="bold red")
    else:
        console.print(f"Invalid resource: {resource}", style="bold red")

def main():
    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)
    api_status = check_api_status()

    console.print(
        Panel(f"ThousandEyes API Status: {api_status}", border_style="orange_red1"),
        style="orange_red1",
    )

    token = os.environ.get("TE_BEARER") or getpass("Bearer Authentication Token: ")
    commands_list = execute_show_resources()
    debug_enabled = False

    while True:
        try:
            command_str = prompt("thousandeyes# ", history=FileHistory(HISTORY_FILE)).lower().strip()
            if not command_str:
                continue

            if command_str == "debug enabled":
                debug_enabled = True
            elif command_str == "debug disabled":
                debug_enabled = False
            elif command_str in ["!", "#"]:
                continue
            elif command_str == "ls" or command_str == "show":
                prefixed_commands = ["show " + command for command in commands_list]
                console.print("\n".join(prefixed_commands))
            elif command_str == "exit":
                break
            elif command_str.startswith("show"):
                resource, file_format, aid, write = parse_command(command_str)
                if resource == "run":
                    table = Table(show_header=True, header_style="bold magenta")
                    table.add_column("Field", style="dim", width=20)
                    table.add_column("Value")
                    table.add_row("Bearer Token", "********" + token[28:])
                    table.add_row("Debug", str(debug_enabled))
                    table.add_row("API Status", api_status)
                    console.print(table)
                elif resource:
                    execute_show_command(resource, token, file_format, aid, write, debug_enabled)
                else:
                    console.print("Invalid 'show' command. Please specify a resource.", style="bold red")
            else:
                console.print("Invalid command. Please try again.", style="bold red")
        except Exception as e:
            console.print(f"An error occurred: {e}", style="bold red")

if __name__ == "__main__":
    main()
