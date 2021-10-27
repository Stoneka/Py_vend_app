#coding: UTF-8
from vender.models import slot_game
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

    def pay_money(self, money, chosen_drink):
        self.money = int(money)
        self.chosen_drink = int(chosen_drink)
        print(self.chosen_drink)
        item_num = self.drinks[self.chosen_drink - 1]
        for i in item_num.values():
            price = int(i)
        for i in item_num.keys():
            item_name = str(i)
        if price <= self.money:
            change = self.money - price
            start_slot = slot_game.SlotGame()
            result = start_slot.play_slot()
            if result:
                print("{}をもう一本プレゼント!!".format(item_name))
            print("お釣りは{}円です".format(change))
        else:
            print("投入金額が足りません")