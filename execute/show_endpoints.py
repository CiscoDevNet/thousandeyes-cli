from .execute_commands import ShowCommand


def show_endpoints(token, file, aid, write):
    endpoints = ShowCommand(token)
    show_endpoints = endpoints("endpoint/agents", file, aid, write)
    return show_endpoints
