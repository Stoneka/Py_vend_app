#coding: UTF-8
from vender.models import vending_machine
class Drink(object):
    def __init__(self, name, fee):
        self.name = name
        self.fee = fee

def drink_registration():
    print("商品を登録してください")
    print("※但し、同じ商品名は登録できません")
    drinks = []
    i = 0
    while i < 3:
        drink_name = check_name_string()
        drink_fee = check_fee_integer()
        drink = Drink(drink_name, drink_fee)
        judge_name = name_validate(drinks, drink, i)
        drinks = judge_name[0]
        drink = judge_name[1]
        i = judge_name[2]
        i += 1
    return drinks

#同名商品の登録を制限する機能を関数として切り出す
def name_validate(drinks, drink, i):
    if drinks == []:
        drinks.append({drink.name : drink.fee})
    else:
        judge_list = []
        for item in drinks:
            if drink.name not in item:
                judge_list.append("True")
            else:
                judge_list.append("False")
        if "False" in judge_list:
            print("その商品は既に登録されています")
            i -= 1
        else:
            drinks.append({drink.name : drink.fee})
    return drinks, drink, i
#商品の金額は整数値でないと登録できない機能
def check_fee_integer():
    drink_fee = input("商品の金額を入力してください")
    try:
        drink_fee = int(drink_fee)
    except:
        print("整数で入力してください")
        return check_fee_integer()
    return drink_fee
#商品の名前は文字でないと登録できない機能
def check_name_string():
    drink_name = input("商品名を入力してください")
    try:
        drink_name = str(drink_name)
    except:
        print("文字で入力してください")
        return check_name_string
    return drink_name
#商品の編集機能（新たに商品を追加する機能）
def add_drink(drinks):
    print("新たに商品を追加します")
    drink_name = check_name_string()
    drink_fee = check_fee_integer()
    drink = Drink(drink_name, drink_fee)
    drinks.append({drink_name : drink_fee})
    return drinks
#商品の編集機能（登録されている商品を削除する機能）
def check_del_num_integer(drinks):
    del_num = input("削除したい商品の番号を選んでください")
    try:
        del_num = int(del_num)
    except:
        print("整数で入力してください")
        return check_del_num_integer()
    if del_num < 0 or del_num > len(drinks):
        print("１〜{}の数字で入力してください".format(len(drinks)))
        return check_del_num_integer(drinks)
    else:
        return del_num
def del_drink(drinks):
    print("登録された商品を削除します")
    del_num = check_del_num_integer(drinks)
    drinks.pop(del_num - 1)
    return drinks
#商品の編集機能（商品の追加・削除を行う選択肢）
def edit_drink(drinks):
    print("商品の編集ができます")
    machine = vending_machine.VendingMachine(drinks)
    machine.show_drinks()
    chose_num = input("商品の追加は【１】、商品の削除は【２】、商品の購入は【３】を入力してください")
    chose_num = int(chose_num)
    if chose_num == 1:
        add_drink(drinks)
        return edit_drink(drinks)
    elif chose_num == 2:
        del_drink(drinks)
        return edit_drink(drinks)
    elif chose_num == 3:
        return
    else:
        print("1~3の整数を入力してください")
        return edit_drink(drinks)
