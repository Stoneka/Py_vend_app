class User(object):
    def __init__(self,money):
        self.money = money
    def choose_drink(self, drinks):
        chosen_drink = check_drink_integer(drinks)
        return chosen_drink
def put_money():
    money = check_money_integer()
    user = User(money)
    print("{}円入っています".format(user.money))
    return user
def check_money_integer():
    money = input("お金を入れてください")
    try:
        money = int(money)
    except:
        print("整数で入力してください")
        return check_money_integer()
    return money
def check_drink_integer(drinks):
    chosen_drink = input("商品番号を選んでください")
    try:
        chosen_drink = int(chosen_drink)
    except:
        print("整数で入力してください")
        return check_drink_integer(drinks)
    if chosen_drink < 0 or chosen_drink > len(drinks):
        print("１〜{}の数字で入力してください".format(len(drinks)))
        return check_drink_integer(drinks)
    else:
        return chosen_drink