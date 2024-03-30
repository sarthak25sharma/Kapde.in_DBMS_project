from db import init_db, init_users


def main():
    init_db()
    init_users()

if __name__ == "__main__":
    main()
