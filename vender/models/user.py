class User(object):
    def __init__(self,money):
        self.money = money
    def choose_drink(self):
        chosen_drink = input("商品番号を選んでください")
        return chosen_drink
def put_money():
    money = check_integer()
    user = User(money)
    print("{}円入っています".format(user.money))
    return user
def check_integer():
    money = input("お金を入れてください")
    try:
        money = int(money)
    except:
        print("整数で入力してください")
        return check_integer()
    return money