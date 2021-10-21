class VendingMachine(object):
    def __init__(self, drinks):
        self.drinks = drinks
    def show_drinks(self):
        print("いらっしゃいませ。以下商品を販売しています")
        for name,fee in self.drinks.items():
            print("【{} 】{}円".format(name, fee))
drinks = {'apple': '100', 'banana': '110', 'orange': '120'}
#drinksは、後ほどDrink_modelから入力する
vending = VendingMachine(drinks)
vending.show_drinks()