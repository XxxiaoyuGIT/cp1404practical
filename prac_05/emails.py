def extract_name(email):
    username = email.split('@')[0]
    name_parts = [part.title() for part in username.split('.')]
    full_name = ' '.join(name_parts)
    return full_name


def main():
    user_data = {}

    while True:
        email = input("Email: ")

        if not email.strip():
            break

        name = extract_name(email)

        response = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if response == '' or response == 'y':
            user_data[email] = name
        else:
            name = input("Name: ")
            user_data[email] = name

    for email, name in user_data.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()
