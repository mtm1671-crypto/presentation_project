from functions.get_file_content import get_file_content


def test():
    result = get_file_content("calculator", "main.py")
    print("Result for main")
    print(result)
    print("")

    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result for 'pkg' calc file")
    print(result)

    result = get_file_content("calculator", "/bin/cat")
    print("Result for '/bin' file:")
    print(result)

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Result for '../' does not exist:")
    print(result)


if __name__ == "__main__":
    test()