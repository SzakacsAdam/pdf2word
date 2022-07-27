from startup_checks import StartupChecks


def main() -> None:
    startup_checks: StartupChecks = StartupChecks()
    result: bool = startup_checks.run()
    print(f"{result=}")


if __name__ == '__main__':
    main()


