def is_vaild_password(text):
    return 8 <= len(text) <= 20


def is_valid_password(new_password):
    pass


def main():
    new_password = "helloworld"
    print(f"{new_password} is a valid password? {is_valid_password(new_password)}")


if __name__ == '__main__':
    main()
