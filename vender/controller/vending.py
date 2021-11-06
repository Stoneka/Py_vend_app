from vender.models import drink
from vender.models import user
from vender.models import vending_machine


def start_vending():
    drinks = drink.drink_registration()
    machine = vending_machine.VendingMachine(drinks)
    machine.show_drinks()
    drink.add_drink(drinks)
    machine.show_drinks()
    drink.del_drink(drinks)
    machine.show_drinks()
    purchaser = user.put_money()
    chosen = purchaser.choose_drink()
    machine.pay_money(purchaser.money, chosen)