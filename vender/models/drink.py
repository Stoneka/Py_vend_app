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
        drink_name = input("商品名を入力してください")
        drink_fee = input("商品の金額を入力してください")
        drink = Drink(drink_name, drink_fee)
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
        i += 1
    return drinks

#def name_validate(drinks, drink):
#    if drinks == []:
#        drinks.append({drink.name : drink.fee})
#    else:
#        judge_list = []
#        for item in drinks:
#            if drink.name not in item:
#                judge_list.append("True")
#            else:
#                judge_list.append("False")
#        if "False" in judge_list:
#            print("その商品は既に登録されています")
#            i -= 1
#        else:
#            drinks.append({drink.name : drink.fee})
#    return drinks