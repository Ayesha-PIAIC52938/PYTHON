"""______________________________________________________________________________________________________________________________________________
    question 3:
        Task1. Make a file (.txt or .csv) that stores inventory (i.e product name, discription, quantity in stock and price) 
        Task2. Write a program thar:
                a.  Asks a user whether he's admin or customer
                b.  For admin: 
                    - Program should be able to add new products to inventory file
                    - Program should have the option to show sale statistics such as sale amount and quantity to the admin
                c.  For customer"
                    - code should enable customer to view products
                    - see product details
                    - provide option for purchase or leave
                        ... in case of putchase if customer required product quantity < available items, allow customer to buy that item.
                            Also update inventory records.
                        ... if customer required product quantity > available items, inform customer about the minimum item he/she can buy.
                            Update sales records if the user proceeds with the purchase.
        
        Admin has the authority to see sales record and add new products

        Customer has access to product list and choice menue

        update inventory records and creat sales recors, showing items sold and its quantity
________________________________________________________________________________________________________________________________________________"""
import inventory 

name = input("Please enter your name: ").title()
user = input(f"\nHello, {name} are you an admin or customer?\nEnter a for admin or c for customer : ").lower()

if user == "c" :
    print(f"\nWelcome {name} (Customer)")
    task = input(f"\nWould you like to view product list? (y/n):").lower()
    if task == "y":
    #_______________________________Displaying product list and details___________________________________________________________________________________
      while True:  
            print("\nPRODUCT LIST:")
            inventory.display_products()
            s_n = int(input("\nTo view the product details type the corrosponding serial number (S/N): "))
            product = inventory.products_details(s_n)

            #_______________________________Purchasing product option____________________________________________________________________________________________
            
            task = input(f"\nWould you like to perchase {product}? (y/n): ").lower()
            if task == "y":
                quantity_required = int(input(f"\nPlease enter the quantity of {product} you would like to perchase: "))
                total_price = inventory.product_purchase (s_n,quantity_required,product)
             
             # _______________________________Update product quantity in thinventory______________________________________________________________________________

                if total_price != 0:
                    inventory.update_inventory(s_n,quantity_required)

             # _______________________________Update sales record_________________________________________________________________________________________________
                
                inventory.sales_record(product,quantity_required,total_price)
                task = input(f"\nWould you like to buy something else? (y/n):").lower()
                if task == "y":
                    continue
                else:
                    print("As you wish, good bye :)")
                    break
            else:
                print("As you wish, good bye :)") 
                break    
    else:
        print("As you wish\nDo come by next time :)")
    
else:
   print(f"Welcome {name} (Admin)")
   task = input(f"\n{name} do you want to add a new product or view sale statistics?\nEnter 'n' for adding new product, 'v' for viewing sale statistics: ").lower()
  
   if task == "n":
    
    #__________________________________Adding new product to inventory____________________________________________________________________________________

    added_new_product,  header, data =     inventory.add_new_product()

    print("\nNew product to be added:", added_new_product)
    print("\n\n")

    #__________________________________Displaying updated inventory__________________________________________________________________________
    
    inventory.display_inventory(header, data)
    #________________________________________________________________________________________________________________________________________

   else:
    print("\nProduct statistics:")
    inventory.product_statistics()