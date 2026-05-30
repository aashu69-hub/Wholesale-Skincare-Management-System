def save_to_file(d):
    with open("products.txt", "w") as file:
        for val in d.values():
            file.write(", ".join([val[0], val[1], str(val[2]), str(val[3]), val[4]]) + "\n")

def write_bill(filename, header, items, grand_total):
    with open(filename, "w") as bill_file:
        bill_file.write(header + "\n")
        for item in items:
            bill_file.write(f"Product: {item['name']}, Qty: {item['quantity']}, Free: {item.get('free_items', 0)}, Total: {item['total']}\n")
        bill_file.write("Grand Total: " + str(grand_total) + "\n")
