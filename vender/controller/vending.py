from vender.models import drink
from vender.models import user
from vender.models import vending_machine


def start_vending():
    drinks = drink.drink_registration()
    machine = vending_machine.VendingMachine(drinks)
    machine.show_drinks()
    edit_vending(drinks, machine)
#商品編集機能を切り出し
def edit_vending(drinks, machine):
    drink.edit_drink(drinks)
    machine.show_drinks()
    purchaser = user.put_money()
    chosen = purchaser.choose_drink(drinks)
    machine.pay_money(purchaser.money, chosen)
    choice_vending(drinks, machine)
#プログラムを継続、終了を選ぶ機能
def choice_vending(drinks, machine):
    choice = input("購入を続けますか？数字を入力してください。【１】続ける【２】終了する")
    try:
        choice = int(choice)
    except:
        print("整数で入力してください")
        return choice_vending(drinks, machine)
    if choice == 1:
        return edit_vending(drinks, machine)
    elif choice == 2:
        return exit()
    else:
        print("1~2で入力してください")
        return choice_vending(drinks, machine)