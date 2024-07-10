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