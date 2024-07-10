# ThousandEyes-CLI Documentation

## Introduction

ThousandEyes-CLI is a Command Line Interface designed to facilitate interactions with the ThousandEyes API. It offers a familiar experience to Cisco device users through a set of `show` commands, mirroring the functionality of a network operating system CLI.

## Problem Statement

APIs can be complex and intimidating for users, often requiring a significant investment of time to learn. This complexity can be a barrier for users of the ThousandEyes platform.

## Solution

ThousandEyes-CLI serves as an intuitive translator between Cisco command-line zsyntax and the ThousandEyes API, streamlining the user experience.

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

To start using ThousandEyes-CLI, you'll need to open your command line terminal and run the Python script. Here's how:

1. Open your command line terminal.
2. Navigate to the directory where the `thousandeyes-cli.py` script is located.
3. Execute the script by typing:

```shell
python thousandeyes-cli.py
```

## Authentication

Before you can start issuing commands, you'll need to enter your Bearer Token. This token is essential for authenticating with the ThousandEyes API and ensuring that your commands are executed successfully.

When prompted, paste your Bearer Token into the console. Make sure to keep your token secure and do not share it with others.

```
# python3.11 thousandeyes-cli.py
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ThousandEyes API Status: Accessible                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
Bearer Authentication Token:
```

## Available Commands

ThousandEyes-CLI offers a range of commands that let you retrieve information from the ThousandEyes API. Here are some examples:

- `show accounts` - Displays account information.
- `show agents` - Lists available agents.
- `show alerts` - Shows current alerts.
- `show alerts rules` - Lists alert rules.
- `show alerts suppression windows` - Shows alert suppression windows.
- `show bgp monitors` - Lists BGP monitors.
- `show credentials` - Displays credential information.
- `show dashboards` - Lists all dashboards.
- `show endpoints` - Shows endpoint data.
- `show endpoints labels` - Lists labels for endpoints.
- `show endpoints tests` - Displays tests for endpoints.
- `show run` - Shows the current running configuration.
- `show tags` - Lists all tags.
- `show tests` - Shows test information.

## Understanding Command Syntax

The ThousandEyes-CLI commands follow a simple and intuitive syntax. To execute a command, type it after the `thousandeyes#` prompt. The general pattern is:

```shell
thousandeyes# [command] [options]
```

### The `show accounts` Command

The `show accounts` command retrieves information about the account groups you have access to. Here's how to use it:

#### Example Command:

```shell
thousandeyes# show accounts
```

#### Example Output:

```json
{
    "accountGroups": [
        {
            "accountGroupName": "user1_account",
            "aid": "1234567",
            "isCurrentAccountGroup": true,
            "isDefaultAccountGroup": true,
            "organizationName": "Organization #1234"
        },
        {
            "accountGroupName": "user2_account",
            "aid": "1234568",
            "isCurrentAccountGroup": false,
            "isDefaultAccountGroup": false,
            "organizationName": "Organization #1234"
        },
        {
            "accountGroupName": "user3_account",
            "aid": "1234569",
            "isCurrentAccountGroup": false,
            "isDefaultAccountGroup": false,
            "organizationName": "Organization #1234"
        }
    ]
}
```

To export the account group information in CSV format, append `file csv` to the command.

#### Example Command:

```shell
thousandeyes# show accounts file csv
```

#### Example Output:

```csv
"accountGroupName","AID"
"user1_account","1234567"
"user2_account","1234568"
"user3_account","1234569"
```

For a human-readable format, use `file human`.

#### Example Command:

```shell
thousandeyes# show accounts file human
```

#### Example Output:

```
Account Group Name: user1_account
AID: 1234567
-----------------------------
Account Group Name: user2_account
AID: 1234568
-----------------------------
Account Group Name: user3_account
AID: 1234569
-----------------------------
```

### The `show dashboards` Command

To display dashboard information for a specific account group, use the `show dashboards` command with the `file human` option and the `aid` parameter.

#### Example Command:

```shell
thousandeyes# show dashboards file human aid 1234567
```

#### Example Output:

```
Dashboard:
  ID: 668ef8976b26111c15d111f2
  Title: Associated Service Recommendations Dashboard
  Created By: 1234567
  Modified By: None
  Modified Date: 2024-07-10T21:09:42Z
  Private: False
  Default for User: False
  Default for Account: False

Dashboard:
  ID: 668ef8976b26111c15d111f3
  Title: Service Health Dashboard TEMPLATE
  Created By: 1234567
  Modified By: 1234567
  Modified Date: 2024-06-03T22:18:32Z
  Private: True
  Default for User: False
  Default for Account: False

Dashboard:
  ID: 668ef8976b26111c15d111f5
  Title: ThousandEyes Built-in: Agent Alerts
  Created By: None
  Modified By: None
  Modified Date: None
  Private: False
  Default for User: False
  Default for Account: False
```

To save the output to a file, append `write` to the command.

#### Example Command:

```shell
thousandeyes# show dashboards file human aid 1234567 write
```

#### Example Output:

```
File created: ./output/dashboards_20240710_153734.human
```

To view the contents of the saved file, navigate to the `output` directory and use the `cat` command.

With these commands, you'll be able to navigate and use ThousandEyes-CLI effectively, making your interactions with the ThousandEyes API much simpler.

## Persisting Environment Variables for Bearer Authentication

To streamline your workflow and eliminate the need to input your Bearer Authentication Token repeatedly, you can save it as a persistent environment variable on your system. Follow the instructions below for your specific operating system:

**macOS and Linux:**

1. Open the Terminal application.
2. Type the following command, replacing `your_token_here` with your actual Bearer Authentication Token:
   ```
   echo 'export TE_BEARER="your_token_here"' >> ~/.bash_profile
   ```
   If you are using a shell other than bash, such as zsh (which is the default on newer versions of macOS), you should instead append the export command to the `~/.zshrc` file:
   ```
   echo 'export TE_BEARER="your_token_here"' >> ~/.zshrc
   ```
3. Save the changes and close the Terminal.
4. To apply the changes immediately, you can source the profile file with the command `source ~/.bash_profile` for bash or `source ~/.zshrc` for zsh.

**Windows:**

1. Press `Win + R`, type `cmd`, and press `Enter` to open the Command Prompt.
2. Enter the following command, again substituting `your_token_here` with your actual token:
   ```
   setx TE_BEARER "your_token_here" /M
   ```
   The `/M` flag sets the variable system-wide. If you omit this flag, the variable will be set for the current user only.
3. Close the Command Prompt.

**Important Notes:**

- After setting the environment variable, you may need to restart your terminal (macOS/Linux) or command prompt (Windows) for the changes to take effect.
- For the changes to be recognized by applications that were running before setting the variable, you may need to restart those applications.
- Environment variables set in this way will persist across system reboots, ensuring your Bearer Authentication Token is always readily available for your sessions.

## Important Disclaimer

ThousandEyes-CLI is a community-created and maintained tool. It is not supported by the ThousandEyes support team or engineering. Users should utilize this tool with the understanding that it is independent of official ThousandEyes resources.

## Conclusion

Congratulations on taking the first step towards simplifying your interactions with the ThousandEyes API using the ThousandEyes-CLI tool. You've equipped yourself with a powerful command-line interface that enhances your productivity and bridges the gap between Cisco CLI familiarity and API complexity.
