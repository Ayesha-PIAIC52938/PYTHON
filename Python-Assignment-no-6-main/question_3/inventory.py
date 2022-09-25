
"""______________________________________________________________________________________________________________________________________________
                                            Inventory module
________________________________________________________________________________________________________________________________________________"""

def extract_inventory():
    
    import csv

    path = "F:\\repo\\Python-Assignment-no-6\\question_3\\inventory.csv"
    with open(path,'r') as f:
        csv_f = csv.reader(f)
        data = []
        header = next(csv_f)
        for rows in csv_f:
            data.append(rows)
    return header,data


def add_new_product():
    import csv

    print("\nAdding new product:")
    product_name = input("Please enter product name:").title()
    product_discription = input(f"Please enter {product_name} discription:")
    product_quantity = input(f"Please enter {product_name} quantity:")
    product_price = input(f"Please enter {product_name} price/product:")

    header,data = extract_inventory()

    sn_new_product = len(data)+1
    new_product = [sn_new_product, product_name, product_discription, product_quantity ,product_price]
         
    new_data= list(data)
    new_data.append(new_product)
   
    path = "F:\\repo\\Python-Assignment-no-6\\question_3\\inventory.csv"
    with open(path,'w', newline="") as w:        
        csv_w = csv.writer(w, delimiter=",")
        csv_w.writerow(header)
        for i in range(len(new_data)):
            csv_w.writerow(new_data[i])
    
    return new_product,  header, new_data 

 
def display_inventory(header,data):
   
    from tabulate import tabulate                       # for printing in table form

    print('-'*191)
    print(tabulate(data, headers = header))
    print('-'*191)


def display_products():
 
    header,data= extract_inventory()  
    products=[]
    index = 0
    for rows in range(len(data)):
        products.append(data[index][0:2])
        index +=1
    display_inventory(header[:2], products)


def products_details(s_n):
    header,data = extract_inventory()   
    # display_products()
    index = s_n-1
    for i in range(len(data)):
        if index == i:
            print(f"\n{index+1}- {data[index][1]}:")
            print(" "*len(data[index][1]) ,f"{data[index][2]}")
    return  data[index][1]  


def update_inventory(s_n,quantity_required):

    import csv

    path = "./question_3/inventory.csv"
    with open(path,'r') as f:
        csv_f = csv.reader(f)
        data = list(csv_f)                              # print("updating product quantity")
        quantity_available = int(data[s_n][3])
        data[s_n][3] = quantity_available-quantity_required
        print(data[s_n][3])

    with open(path,'w', newline="") as w:
        csv_w = csv.writer(w, delimiter=",")
        for i in range(len(data)):
            csv_w.writerow(data[i])


def product_purchase (s_n,quantity_required,product):
    
    header,data = extract_inventory()    

    if quantity_required > int(data[s_n-1][3]):      # product quantity in stock: data[s_n-1][3]

        print(f"\nSorry your required quantity of {product} is more then whats currently in stock\nCurrently {product} available in stock: {data[s_n-1][3]} articles")
        total_price = 0

    else:
        total_price = quantity_required*int(data[s_n-1][4])  #price of product: data[s_n-1][4]

        print(f"\nTotal price for {quantity_required} articles of {product} is: Rs.{total_price}/-")        
    return total_price


def sales_record(product,quantity_required,total_price):
    import csv
    wr =[product,quantity_required,total_price]
    path = "./question_3/sales.csv"
    
    with open(path,"a") as sales_r:
        write_record = csv.writer(sales_r)
        write_record.writerow(wr)


def product_statistics():
    import csv
    path = "./question_3/sales.csv"
    try:
        with open(path,"r") as p_s:
            csv_ps = csv.reader(p_s)
            updated_data = []
            for rows in csv_ps:
                updated_data.append(rows)
        header = ["Product","Quantity Purchased","Total Price(Rs.)"]
        display_inventory(header,updated_data)
    except FileNotFoundError:
        print("Sorry no customer visited yet so sale statictics not available at the moment ")
 
