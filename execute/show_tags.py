from .execute_commands import ShowCommand


def show_tags(token, file, aid, write):
    tags = ShowCommand(token)
    show_tags = tags("tags", file, aid, write)
    return show_tags
