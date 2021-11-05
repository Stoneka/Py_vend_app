#coding: UTF-8
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