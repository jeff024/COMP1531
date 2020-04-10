def scan():
    my_list = []
    for c in ['a', 'b', 'c', 'd', 'e']:
        i = input(f'Enter {c}: ')
        i = int(i)
        my_list.append(i)
    return my_list

def product(l, start, end):
    product = 1
    for i in range(start, end):
        product = product * my_list[i]
    print(f"  {product}")

if __name__ == '__main__':

    my_list = scan()
    print("Minimum: " + str(min(my_list)))
    print("Product of first 4 numbers: ")
    product(my_list, 0, 4)
    print("Product of last 4 numbers")
    product(my_list, 1, 5)