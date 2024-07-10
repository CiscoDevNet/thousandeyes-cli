# ThousandEyes-CLI Documentation

## Introduction

ThousandEyes-CLI is a Command Line Interface designed to facilitate interactions with the ThousandEyes API. It offers a familiar experience to Cisco device users through a set of "show" commands, mirroring the functionality of a network operating system CLI.

## Problem Statement

APIs can be complex and intimidating for users, often requiring a significant investment of time to learn. This complexity can be a barrier for users of the ThousandEyes platform.

## Solution

ThousandEyes-CLI serves as an intuitive translator between Cisco command-line syntax and the ThousandEyes API, streamlining the user experience.

## What You’ll Learn

By using ThousandEyes-CLI, you will learn how to:

- Navigate and execute commands in a CLI environment.
- Interact with the ThousandEyes API using simplified commands.
- Output and manage data in various formats like JSON, YAML, CSV, and human-readable text.
- Set and use environment variables to streamline your workflow.

## What You’ll Need

To use ThousandEyes-CLI, you will need:

- A computer with Python installed.
- Access to the command line terminal.
- The ThousandEyes API Bearer Token.
- Basic knowledge of command-line operations and syntax.

## Key Features

- **Usability**: Designed for ease of use and extensibility.
- **Single Input Bearer Token**: Only needs the ThousandEyes API Bearer Token once per session.
- **Multiple Data Formats**: Supports JSON, YAML, CSV, and human-readable output.
- **Data Output Redirect**: Allows users to direct output to either the console or a file.

## Getting Started

Before using ThousandEyes-CLI, ensure Python is installed on your system. Install the necessary Python libraries with the following command:

```shell
pip install -r requirements.txt
```

## Dependencies

ThousandEyes-CLI requires these Python libraries:

- os
- re
- readline
- socket
- getpass
- rich
- importlib
- requests
- yaml
- json
- datetime
- jinja2

## Usage Instructions

1. Open a command line terminal.
2. Navigate to the directory with the thousandeyes-cli.py script.
3. Execute the script:

```shell
python thousandeyes-cli.py
```

## Available Commands

- `show accounts`
- `show agents`
- `show alerts`
- `show alerts rules`
- `show alerts suppression windows`
- `show bgp monitors`
- `show credentials`
- `show dashboards`
- `show endpoints`
- `show endpoints labels`
- `show endpoints tests`
- `show run`
- `show tags`
- `show tests`

## Examples

- Display all accounts:

```shell
show accounts
```

- Change output format to CSV:

```shell
show accounts file csv
```

- Filter information by AID:

```shell
show endpoints file human aid 1234
```

- Save output to a file:

```shell
show endpoints file human aid 1234 write
```

## Environment Variable

To avoid entering the Bearer Authentication Token each time, set the `TE_BEARER` environment variable:

- On macOS:

```shell
export TE_BEARER=your_token_here
```

- On Windows:

```shell
setx TE_BEARER "your_token_here"
```

*Replace `your_token_here` with your actual Bearer Authentication Token.*

**Note**: After setting the environment variable, restart your terminal or command prompt.

## Important Disclaimer

ThousandEyes-CLI is a community-created and maintained tool. It is not supported by the ThousandEyes support team or engineering. Users should utilize this tool with the understanding that it is independent of official ThousandEyes resources.

## Conclusion

Congratulations on taking the first step towards simplifying your interactions with the ThousandEyes API using the ThousandEyes-CLI tool. You've equipped yourself with a powerful command-line interface that enhances your productivity and bridges the gap between Cisco CLI familiarity and API complexity.
