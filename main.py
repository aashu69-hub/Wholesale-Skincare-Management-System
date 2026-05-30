from read import read_products
from operations import sell_products, purchase_stock

d = read_products()

print("\n" * 2)
print("\t" * 10 + "WeCare Wholesale")
print("\n")
print("\t" * 8 + "Lubhu, Lalitpur | Phone No: 9741743485")
print("\n")
print("-" * 200)
print("\t" * 7 + "Hello Admin! Great to have you back. Hope you’re having a fantastic day!")
print("-" * 200 + "\n")

main_loop = True
while main_loop:
    print("=" * 200)
    print("Main Menu:")
    print("1. Sell products to a customer")
    print("2. Purchase stock from a manufacturer")
    print("3. Exit the system")
    print("=" * 200 + "\n")

    try:
        option = int(input("Enter the option to continue: "))
    except:
        print("Invalid input. Please enter a number.")
        continue

    if option == 1:
        sell_products(d)
    elif option == 2:
        purchase_stock(d)
    elif option == 3:
        main_loop = False
        print("Thank you for using the system. Have a good day, Admin!")
    else:
        print("Invalid option. Please try again.")
