order_list = []
storage_list = []

class new_order:
    def __init__(self, name, category, quantity):
        self.buyer_name = name
        self.category = category
        self.quantity = quantity


class customer:
    def __init__(self, name):
        self.name = name
    def place_order(self, category, quantity):
        print(f'{self.name} ordered {quantity} {category}s')
        global order_list
        global storage_list
        cus_order = new_order(self.name, category, quantity)
        pended = False
        for order in order_list:
            if order.category == category:
                order_list.append(cus_order)
                pended = True
        if not pended:
            for fruit in storage_list:
                if fruit.category == category:
                    if fruit.quantity < quantity:
                        order_list.append(cus_order)
                        print(f'{self.name}\'s order is pending')
                        return
                    elif fruit.quantity == quantity:
                        fruit.quantity -= quantity
                        print(f'{self.name}\'s order is successful and no more {fruit.category} left')
                        return
                    else:
                        fruit.quantity -= quantity
                        print(f'{self.name}\'s order is successful and there are {fruit.quantity} left')
                        return
        # if the required fruit doesn't exists
        order_list.append(cus_order)
        print(f'{self.name}\'s order is pending')

class fruit:
    def __init__(self, category, quantity):
        self.category = category
        self.quantity = quantity
    def add(self, quantity):
        self.quantity += quantity

class wholesaler:
    def __init__(self, name):
        global storage_list
        self.fruit_all = storage_list
        self.name = name
    def fulfill(self, category, quantity):
        print(f'{self.name} fulfilled {quantity} {category}s')
        found = False
        for goods in self.fruit_all:
            if goods.category == category:
                found = True
                goods.add(quantity)
        if not found:
            goods = fruit(category, quantity)
            self.fruit_all.append(goods)
        global order_list
        global storage_list
        for order in order_list:
            for goods in storage_list:
                if goods.category == order.category:
                    if goods.quantity == order.quantity:
                        goods.quantity -= order.quantity
                        order_list.remove(order)
                        print(f'{order.buyer_name}\'s order is successful and no more {goods.category} left')
                    else:
                        goods.quantity -= order.quantity
                        print(f'{order.buyer_name}\'s order is successful there are {goods.quantity} left')

if __name__ == "__main__":
    jeff = wholesaler('jeff')
    jeff.fulfill('apple', 5)
    # print(jeff.fruit_all[0].category)
    # print(jeff.fruit_all[0].quantity)
    jeff.fulfill('apple', 5)
    tim = customer('tim')
    tim.place_order('apple', 5)
    tim.place_order('apple', 5)
    tim.place_order('banana', 5)
    jeff.fulfill('apple', 5)
    jeff.fulfill('banana', 10)



