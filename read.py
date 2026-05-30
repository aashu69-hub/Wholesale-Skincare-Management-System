def read_products():
    d = {}
    with open("products.txt", "r") as file:
        data = file.readlines()
        p_id = 1
        for line in data:
            line = line.replace("\n", "").split(",")
            d[p_id] = line
            p_id += 1
    return d
