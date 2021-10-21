class User(object):
    def __init__(self,money):
        self.money = money

def put_money():
    money = input("お金を入れてください")
    user = User(money)
    print("{}円入っています".format(user.money))
put_money()