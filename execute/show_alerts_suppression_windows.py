from .execute_commands import ShowCommand


def show_alerts_suppression_windows(token, file, aid, write):
    alerts_suppression_windows = ShowCommand(token)
    show_alerts_suppression_windows = alerts_suppression_windows(
        "alert-suppression-windows", file, aid, write
    )
    return show_alerts_suppression_windows
