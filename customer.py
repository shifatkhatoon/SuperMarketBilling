from os import system
from models import Product, session
from product import show_products

products = session.query(Product)


def customer_menu():
    show_products()
    print("\n======================================================")
    print("\n\t\t\t\t\t\t Place Order")
    print("\n======================================================")
    more = 'y'
    data = {}
    while more == 'y':
        p_no = int(input("\n\n Enter the P.NO. of the Item:\t"))
        if not products.filter_by(id=p_no).first():
            print("Enter valid product id")
            continue
        count = int(input("\n\n How many units? :\t"))
        data[p_no] = count
        more = str(input("Do You Want To Order Another Product ? (y/n)")).strip()
        more = more
        pass
    print(data)
    print("\n======================================================")
    input("Thank you for shopping press enter to generate Invoice: ")
    system('clear')
    generate_invoice(data)
    
    
def generate_invoice(data):
    total = 0
    print("\n\n********************************INVOICE************************\n")

    print("\tItem\t\tQuantity\tPrice \tAmount \t\tAmount after discount\n")
    for id in data:
        pr = products.filter_by(id=id).first()
        amt = data[id] * pr.price
        damt = amt - amt * (pr.discount / 100)
        print("\t{}\t\t{}\t{} \t{} \t\t{}".format(pr.name, data[id], pr.price, amt, damt))
        total+=damt
    print("\n\n\t\t\t\t\t\t\t\t\t\t Total:= Rs. ",total)
    
    
    
