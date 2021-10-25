import random

class SlotGame(object):
    def play_slot(self):
        result = []
        i = 1
        while i < 4:
            result.append(random.randint(0, 9))
            i += 1
        result = map(str, result)
        result = "".join(result)
        print("スロットの結果は{}です".format(result))
        if result[0] == result[1] and result[0] == result[2]:
            print("おめでとう！アタリです")
        else:
            print("残念･･･ハズレです")
#start_slot = SlotGame()
#start_slot.play_slot()

