from random import *
lst=list(range(1,21))
shuffle(lst)

winners = sample(lst,4)
print("---당첨자 발표---")
print("치킨 당첨자:{0}".format(winners[0]))
print("커피 당첨자:{0}".format(winners[1:]))
print("---축하합니다.---")