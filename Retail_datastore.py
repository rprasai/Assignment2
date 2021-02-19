import RetailItemClass


def main():
    item_num = int(input("Enter the total number of items: "))
    item_list = itemlist(item_num)
    display_items(item_list)


def itemlist(num_item):
    retail_list = []
    for count in range(0, num_item):
        print("item #" + str(count + 1) + ":")
        desc = input("Enter the product description: ")
        unit = int(input("Product Unit: "))
        price = float(input("Product Price: "))
        print()

        item_detail = RetailItemClass.Retail_Item(desc, unit, price)
        retail_list.append(item_detail)
    return retail_list


def display_items(itemlist):
    count = 0
    for item in itemlist:
        print("item #" + str(count + 1) + ":")
        print(item.get_desc())
        print(item.get_unit())
        print(item.get_price())
        print()


main()