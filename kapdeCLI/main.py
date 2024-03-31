import db
import rich.text
import rich.console


def print_logo():
    logo_lines = [f"   / ___      ___        ___        ___   /      ___    ",
                  f"  //\ \     //   ) )   //   ) )   //   ) /     //___) ) ",
                  f" //  \ \   //   / /   //___/ /   //   / /     //        ",
                  f"//    \ \ ((___( (   //         ((___/ /     ((____     "]

    colors = ["orange3",
              "light_salmon3",
              "light_pink3",
              "pink3",
              "plum3"]

    console = rich.console.Console()
    for i in range(len(logo_lines)):
        text = rich.text.Text.from_ansi(logo_lines[i])
        text.stylize(f"bold {colors[i]}", 0, len(logo_lines[0]))
        console.print(text, justify="center")


def print_admin_menu() -> str:
    print("ADMIN MENU")
    print("1) View products")
    print("2) Add products")
    print("3) Remove products")
    print("4) View all tables")
    print("5) Exit")
    return input("Enter your choice: ")


admin_menu_func = {"1": db.view_products,
                   "2": db.add_product,
                   "3": db.remove_product,
                   "4": db.print_all_tables, }


def admin_menu():
    while True:
        choice = print_admin_menu().strip()
        if choice == "5":
            return
        if choice not in admin_menu_func:
            print("Invalid choice")
        else:
            admin_menu_func[choice]()


def print_user_menu() -> str:
    print("USER MENU")
    print("1) View products")
    print("2) Search products")
    print("3) View cart")
    print("4) Add product to cart")
    print("5) Place order")
    print("6) Exit")
    return input("Enter your choice: ")


user_menu_func = {"1": db.view_products,
                  "2": db.search_product,
                  "3": db.get_user_cart,
                  "4": db.add_product_to_cart,
                  "5": db.place_order, }


def user_menu(user_id: int):
    while True:
        choice = print_user_menu().strip()
        if choice == "6":
            return
        if choice not in user_menu_func:
            print("Invalid choice")
        elif choice == "3":
            user_menu_func[choice](user_id)
        else:
            user_menu_func[choice]()


def login():
    print("Enter program as: ")
    print("1. User")
    print("2. Admin")
    print("3. Exit")
    key = input("Enter your choice: ").strip()
    if key == "1":
        a = True
        while a:
            print("USER LOGIN MODE (Press x to go back)")
            input_key = input("Enter your id: ").strip().lower()

            if input_key == "x":
                print("Going back...")
                break
            if not input_key.isnumeric():
                print("Please enter a valid ID")
                break

            user_id = int(input_key)
            password = input("Enter your password: ").strip()
            if db.login_as_user(user_id, password):
                user_menu(user_id)
                a = False

    elif key == "2":
        print("ADMIN LOGIN MODE")
        while True:
            password = input("Enter admin password: ").strip()
            if password == "pass":
                admin_menu()
            break

    elif key == "3":
        db.commit_all()
        exit()
    else:
        print("Invalid input")


def main():
    print_logo()
    db.init_db()
    db.populate()
    while True:
        login()


if __name__ == "__main__":
    main()
