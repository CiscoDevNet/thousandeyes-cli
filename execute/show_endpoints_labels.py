from .execute_commands import ShowCommand


def show_endpoints_labels(token, file, aid, write):
    endpoints_labels = ShowCommand(token)
    show_endpoints_labels = endpoints_labels("endpoint/labels", file, aid, write)
    return show_endpoints_labels
