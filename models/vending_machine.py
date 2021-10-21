class VendingMachine(object):
    def __init__(self, drinks):
        self.drinks = drinks

    def show_drinks(self):
        print("いらっしゃいませ。以下商品を販売しています")
        num = 1
        for item in self.drinks:
            for name,fee in item.items():
                print("【{}】{}:{}円".format(num, name, fee))
                num += 1

    def pay_money(self):
        chosen_drink = 1
        money = 1000
        item_num = self.drinks[chosen_drink - 1]
        for i in item_num.values():
            price = int(i)
        change = money - price
        print("お買い上げありがとうございます、お釣りは{}円です".format(change))


drinks = [{'apple': '100'}, {'banana': '110'}, {'orange': '120'}]
#drinksは、後ほどDrink_modelから入力する
vending = VendingMachine(drinks)
vending.show_drinks()
vending.pay_money()