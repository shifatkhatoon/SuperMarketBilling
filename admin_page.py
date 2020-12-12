from os import system
from models import Product, Department, session
from main import main

products = session.query(Product)

def admin_menu():
  while True:
      print('------------------Welcome to the supermarket------------------')
      print('1. View Products\n2. Add Products for sale\n3. Delete Products\n4. Search Products \n5. Edit Products\n6. Exit')
      choice = input('Enter the number of your choice : ')

      if choice == '1' :
          print('------------------View Products------------------')
          print('The number of products in the inventory are : ',len(products))
          for product in products:
            print("{}\t\t{}\t\t\t{}\t\t{}%".format(product.id, product.name, str(product.price), product.discount))

      elif choice == '2' :
          print('------------------Add Products------------------')
          print('To add an item provide following product details')
          product = {}
          product['name'] = input('Product name : ')
          while True:
              try:
                  product['count'] = int(input('Item quantity : '))
                  break
              except ValueError:
                  print('Quantity should only be in digits')
          while True:
              try:
                  product['price'] = float(input('Price $ : '))
                  break
              except ValueError:
                  print('Price should only be in digits')
          while True:
              try:
                  product['discount'] = float(input('discount : '))
                  break
              except ValueError:
                  print('Discount should only be in digits')
          dept_name = input('Product Department Name : ')
          create_dept = Department(name=dept_name)
          session.add(create_dept)
          session.commit()
          new_product = Product(
                      name=product.name.lower(),
                      price=product.price,
                      discount=product.discount,
                      count=product.count,
                      department_id=create_dept.id
                      )
          session.add(new_product)
          session.commit()
          print('Product has been successfully added.')

      elif choice == '3' :
          print('------------------Delete Products------------------')
          for product in products:
            print("{}\t\t{}\t\t\t{}\t\t{}%".format(product.id, product.name, str(product.price), product.discount))

          delete_product = input('which item do you want to Delete? Enter name : ').lower()
          session.delete(Product.query.filter_by(name=delete_product))
          session.commit()

      elif choice == '5' :
          print('------------------Edit Products------------------')
          
          for product in products:
            print("{}\t\t{}\t\t\t{}\t\t{}%".format(product.id, product.name, str(product.price), product.discount))
            
          product_name = input('Enter the name of the product that you want to edit : ').lower()
          edit_product = Product.query.filter_by(name=product_name).first()
       
          new_details = {}
          
          edit_product.name = input('')
          session.commit()

      elif choice == '6' :
          main()

      else: 
           print('You entered an invalid option')
