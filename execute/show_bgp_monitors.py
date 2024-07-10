from .execute_commands import ShowCommand


def show_bgp_monitors(token, file, aid, write):
    bgp_monitors = ShowCommand(token)
    show_bgp_monitors = bgp_monitors("monitors", file, aid, write)
    return show_bgp_monitors
