from os import system
from models import Product, session

products = session.query(Product)


def show_products():
    print("\n\n\t\tSelect Items\n\n")

    print("========================================================================\n")
    print("P.NO.\t\tNAME\t\t\t\tPRICE\t\tDiscount\n")
    print("========================================================================\n")

    for product in products:
        print("{}\t\t{}\t\t\t{}\t\t{}%".format(product.id, product.name, str(product.price), product.discount))
