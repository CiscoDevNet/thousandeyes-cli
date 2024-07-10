from .execute_commands import ShowCommand


def show_credentials(token, file, aid, write):
    credentials = ShowCommand(token)
    show_credentials = credentials("credentials", file, aid, write)
    return show_credentials
