from .execute_commands import ShowCommand


class ShowTests(ShowCommand):
    def __call__(self, resource, file, aid, write):
        if not write:
            return "This command only works with write argument"
        return super().__call__(resource, file, aid, write)


def show_tests(token, file, aid, write):
    tests = ShowTests(token)
    show_tests = tests("tests", file, aid, write)
    return show_tests
