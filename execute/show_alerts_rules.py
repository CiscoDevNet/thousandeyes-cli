from .execute_commands import ShowCommand


def show_alerts_rules(token, file, aid, write):
    alerts_rules = ShowCommand(token)
    show_alerts_rules = alerts_rules("alerts/rules", file, aid, write)
    return show_alerts_rules
