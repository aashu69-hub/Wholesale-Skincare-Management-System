from datetime import datetime
from write import save_to_file, write_bill

def display_products(d):
    print("*" * 110)
    print("S.N    \tProduct Name        \tCompany Name        \tQuantity\tPrice   Country")
    print("=" * 110)
    
    i = 1  
    for key in d:
        value = d[key]
        sn = str(i)
        pname = value[0]
        cname = value[1]
        qty = value[2]
        price = value[3]
        country = value[4]

        
        print(sn + "      \t" +
              pname + " " * (20 - len(pname)) + "\t" +
              cname + " " * (20 - len(cname)) + "\t" +
              qty + "\t\t" +
              price + "\t" +
              country)
        
        i += 1  
    print("-" * 110)


def sell_products(d):
    print("-" * 50)
    print("For Bill Generation, enter customer details:")
    print("-" * 50 + "\n")

    # Customer Name Validation
    while True:
        name = input("Customer Name: ").strip()
        if name == "":
            print("Name cannot be empty.\n")
        elif name.isdigit():
            print("Name cannot be only numbers.\n")
        else:
            break

    print()

    # Customer Phone Validation
    while True:
        phone_number = input("Customer Phone Number: ")
        if phone_number.isdigit() and len(phone_number) == 10:
            break
        else:
            print("Invalid phone number. It must be exactly 10 digits.\n")

    sold_items = []
    grand_total = 0

    while True:
        display_products(d)
        try:
            pid = int(input("Enter Product ID to sell: "))
            if pid not in d:
                raise ValueError
        except:
            print("Invalid Product ID.")
            continue

        try:
            qty = int(input("Enter quantity to sell: "))
        except:
            print("Invalid quantity.")
            continue

        stock_qty = int(d[pid][2])
        free = 1 if qty == 3 else 0  # Only 1 free item for exactly 3 purchased
        total_deduct = qty + free

        if qty <= 0 or total_deduct > stock_qty:
            print("Insufficient stock.")
            continue

        print("Dear " + name + ", you received " + str(free) + " free item(s).")
        d[pid][2] = str(stock_qty - total_deduct)

        item_name = d[pid][0]
        item_price = int(d[pid][3]) * 2
        total = item_price * qty
        grand_total += total

        sold_items.append({
            'name': item_name,
            'quantity': qty,
            'free_items': free,
            'price': item_price,
            'total': total
        })

        more = input("Sell more products? (yes/no): ").lower()
        if more != "yes":
            break

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bill_text = "Final Bill for " + name + "\nPhone: " + phone_number + "\nDate & Time: " + now
    bill_file = "sale_bill_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
    
    print("\n" + "=" * 110)
    print(bill_text)
    print("=" * 110)
    for item in sold_items:
        print("Product: " + item['name'])
        print("Quantity: " + str(item['quantity']))
        print("Free Items: " + str(item['free_items']))
        print("Price (Per Item): " + str(item['price']))
        print("Total Cost: " + str(item['total']))
        print("-" * 110)
    print("Grand Total: " + str(grand_total))
    print("=" * 110)
    
    write_bill(bill_file, bill_text, sold_items, grand_total)
    save_to_file(d)

def purchase_stock(d):
    print("Available products for restocking:")
    display_products(d)

    purchase_items = []
    grand_total = 0

    while True:
        try:
            pid = int(input("Enter the product ID to restock: "))
            if pid not in d:
                raise ValueError
        except:
            print("Invalid Product ID.")
            continue

        try:
            qty = int(input("Enter quantity to add: "))
            if qty <= 0:
                raise ValueError
        except:
            print("Quantity must be a positive number.")
            continue

        d[pid][2] = str(int(d[pid][2]) + qty)
        item_name = d[pid][0]
        item_price = int(d[pid][3])
        total = item_price * qty
        grand_total += total

        purchase_items.append({
            'name': item_name,
            'quantity': qty,
            'price': item_price,
            'total': total
        })

        more = input("Purchase more products? (yes/no): ").lower()
        if more != "yes":
            break

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bill_text = "Purchase Bill\nDate & Time: " + now
    bill_file = "purchase_bill_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"

    print("\n" + "=" * 110)
    print(bill_text)
    print("=" * 110)
    for item in purchase_items:
        print("Product: " + item['name'])
        print("Quantity: " + str(item['quantity']))
        print("Price (Per Item): " + str(item['price']))
        print("Total Cost: " + str(item['total']))
        print("-" * 110)
    print("Grand Total: " + str(grand_total))
    print("=" * 110)

    write_bill(bill_file, bill_text, purchase_items, grand_total)
    save_to_file(d)
