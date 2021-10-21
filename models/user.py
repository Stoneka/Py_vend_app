class User(object):
    def __init__(self,money):
        self.money = money
    def choose_drink(self):
        chosen_drink = input("商品番号を選んでください")
def put_money():
    money = input("お金を入れてください")
    user = User(money)
    print("{}円入っています".format(user.money))
    user.choose_drink()
put_money()