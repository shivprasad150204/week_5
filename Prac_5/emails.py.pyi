"""
Email and Name Storage
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirm not in ("", "y"):
            name = input("Name: ").strip().title()
        email_to_name[email] = name
        email = input("Email: ")

    print("\nStored Emails and Names:")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Extract name from email."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = ' '.join(parts).title()
    return name


if __name__ == "__main__":
    main()
