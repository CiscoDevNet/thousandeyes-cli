from .execute_commands import ShowCommand


def show_endpoints_tests(token, file, aid, write):
    endpoints_tests = ShowCommand(token)
    show_endpoints_tests = endpoints_tests(
        "endpoint/tests/scheduled-tests", file, aid, write
    )
    return show_endpoints_tests
