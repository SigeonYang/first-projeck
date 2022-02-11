#클래스 == 붕어빵 틀이다.
#연관이 있는 변수와 함수의 집합

class Unit:
    def __init__(self,name,hp,damage): #
        self.name = name #맴버변수 = 클래스 내에서 정의된 변수
        self.hp=hp #맴버변수를 초기화
        self.damage=damage #맴버변수를 초기화
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))

marine1 = Unit("마린", 40 , 5)
marine2 = Unit("마린",40,5)
tank = Unit("탱크",150,35)
tanck2 = Unit("탱크",150,35)

# 클래스로 부터 만들어지는 것들을 객체라고 한다.
# 마린과 탱크는 유닛클래스의 인스턴스다
# 객체가 생성될 때는 init함수에 적용된 개수와 똑같이 줘야한다.

# 레이스 : 클로킹

wraith1 = Unit("레이스",80,5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
#맴버 변수를 외부에서 쓸 수 있음

wraith2 = Unit("빼앗은 레이스",80,5)
wraith2.clockig = True #객체에 변수를 외부에서 추가로 만들어줌
if wraith2.clockig == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))