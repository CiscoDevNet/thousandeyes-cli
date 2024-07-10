from .execute_commands import ShowCommand


def show_dashboards(token, file, aid, write):
    dashboards = ShowCommand(token)
    show_dashboards = dashboards("dashboards", file, aid, write)
    return show_dashboards
