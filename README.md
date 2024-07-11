# ThousandEyes-CLI Documentation

## Introduction

ThousandEyes-CLI is a Command Line Interface that makes it easier to work with the ThousandEyes API, offering `show` commands similar to those used in Cisco network device CLIs.

## Problem Statement

APIs can be difficult and overwhelming, which can discourage users from using the ThousandEyes platform.

## Solution

ThousandEyes-CLI turns Cisco CLI commands into ThousandEyes API calls, making the experience more straightforward for users.

## What You’ll Learn

With ThousandEyes-CLI, you will learn how to:

- Use CLI commands and navigate the interface.
- Interact with the ThousandEyes API more easily.
- Display data in formats like JSON, YAML, CSV, or plain text.
- Set and apply environment variables to make your work more efficient.

## What You’ll Need

To get started with ThousandEyes-CLI, you need:

- A computer with Python.
- Access to a command line terminal.
- The ThousandEyes API Bearer Token.
- A basic understanding of CLI commands and syntax.

## Key Features

- **Ease of Use**: Simple design for straightforward use and customization.
- **Single Bearer Token Entry**: Enter the ThousandEyes API Bearer Token just once each session.
- **Various Data Formats**: Choose from JSON, YAML, CSV, or text for output.
- **Output Control**: Send output to the screen or save it to a file.

## Dependencies

ThousandEyes-CLI needs the following Python libraries:

- os
- re
- readline
- socket
- getpass
- rich
- importlib
- requests
- pyyaml
- json
- datetime
- jinja2
- prompt_toolkit

Use Python 3.11 for compatibility with ThousandEyes-CLI.

## Getting Started

To set up ThousandEyes-CLI:

1. **Download the ZIP File**

Download the ZIP file with the source code from this repository.

2. **Unzip the File**

Find the ZIP file on your computer and extract it. Use "Extract All..." on Windows or double-click the file on macOS.

3. **Navigate to the Directory**

Use the command line to go to the extracted files' directory:

```shell
cd path/to/thousandeyes-cli
```

Replace `path/to/thousandeyes-cli` with the actual directory path.

4. **Install Dependencies**

In the ThousandEyes-CLI directory, there's a `requirements.txt` file. Install the listed libraries with:

```shell
pip install -r requirements.txt
```

## Usage Instructions

To use ThousandEyes-CLI, follow these steps:

1. Open your command line terminal.
2. Go to the folder with `thousandeyes-cli.py`.
3. Run the script with:

```shell
python thousandeyes-cli.py
```

## Authentication

Authenticate using a Bearer Token from the ThousandEyes API.

Get your Bearer Token by following the instructions in the ThousandEyes API documentation:

[ThousandEyes API Authentication Guide](https://developer.cisco.com/docs/thousandeyes/authentication/#authentication)

You can input your Bearer Token each time or save it as an environment variable for repeated use, as explained in the "Persisting Environment Variables for Bearer Authentication" section.

When asked, enter your Bearer Token in the console. Keep your token private and don't share it.

```
# python3.11 thousandeyes-cli.py
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ThousandEyes API Status: Accessible                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
Bearer Authentication Token:
```

**Note:** If you change or regenerate your Bearer Token, you will need to update your environment variable with the new token.

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

### Emphasizing the Importance of the `aid` Parameter

The `aid` parameter is crucial when you need to fetch information specific to a certain account group. Without specifying the correct `aid`, you may not retrieve the relevant data for the account group you intend to manage or analyze. The `aid` Parameter can be obtained with the following command.

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

## Persisting Environment Variables for Bearer Authentication

Save your Bearer Token as an environment variable to avoid entering it every time:

**macOS and Linux:**

1. Open Terminal.
2. Run this command, replacing `your_token_here` with your token:
   ```
   echo 'export TE_BEARER="your_token_here"' >> ~/.bash_profile
   ```
   For zsh (default on newer macOS), use `~/.zshrc` instead:
   ```
   echo 'export TE_BEARER="your_token_here"' >> ~/.zshrc
   ```
3. Restart the Terminal.

**Windows:**

1. Press `Win + R`, type `cmd`, and hit `Enter`.
2. Type this command with your token:
   ```
   setx TE_BEARER "your_token_here" /M
   ```
   Use `/M` for a system-wide variable, or omit it for the current user only.
3. Restart Command Prompt.

**Notes:**

- Restart your terminal or command prompt to apply the changes.
- These variables will remain after system restarts, keeping your token ready for use.

## Important Disclaimer

ThousandEyes-CLI is community-created and not officially supported by ThousandEyes. Use it knowing it's separate from official ThousandEyes tools.

## Conclusion

You're now ready to use ThousandEyes-CLI to make working with the ThousandEyes API easier, leveraging your Cisco CLI knowledge.
