from .execute_commands import ShowCommand


def show_alerts(token, file, aid, write):
    alerts = ShowCommand(token)
    show_alerts = alerts("alerts", file, aid, write)
    return show_alerts
