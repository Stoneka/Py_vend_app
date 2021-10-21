#coding: UTF-8
class Drink(object):
    def __init__(self, name, fee):
        self.name = name
        self.fee = fee

def drink_registration():
    print("商品を登録してください")
    drinks = []
    i = 0
    while i < 3:
        drink_name = input("商品名を入力してください")
        drink_fee = input("商品の金額を入力してください")
        drink = Drink(drink_name, drink_fee)
        drinks.append({drink.name : drink.fee})
        i += 1
    return drinks
