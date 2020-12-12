from os import system
# from models import Product, Department, Invoice, session
from product import show_products
from customer import customer_menu
from admin_page import admin_menu

#
# create_dept = Department(name="Cosmetic")
# session.add(create_dept)
# session.commit()
#
# vaseline = Product(
#     name="Vaseline",
#     price=100,
#     discount=0,
#     count=20,
#     department_id=create_dept.id
# )
#
# session.add(vaseline)
# session.commit()

def show_intro():
    print("\n\n\n\t\t\t\t\t Welcome to Supermarket Billing \n\t\t\t\t\t Press Enter key to enter!!")

    print("\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\tMade by: Shifat ")

    input()


if __name__ == "__main__":
    show_intro()
    while True:
        system('clear')
        print("\n\n\n\tSelect your kind")
        print("\n\n\t1. Customer")
        print("\n\n\t2. Admin")
        print("\n\n\t3. Products")
        print("\n\n\t4. Exit")
        print("\n\n\tPlease select an option(1-4)")
        option = int(input())
        if option == 1:
            system('clear')
            customer_menu()
        if option == 2:
            admin_menu()
        if option == 3:
            show_products()
        else:
            break
