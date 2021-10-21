class User(object):
    def __init__(self,money):
        self.money = money
    def choose_drink(self):
        chosen_drink = input("商品番号を選んでください")
        return chosen_drink
def put_money():
    money = input("お金を入れてください")
    user = User(money)
    print("{}円入っています".format(user.money))
    return user