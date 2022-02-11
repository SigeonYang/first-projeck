#일반유닛
class Unit:
    def __init__(self,name,hp,speed):
        self.name = name 
        self.hp=hp 
        self.speed = speed
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))
#공격유닛
class AttackUnit(Unit):
    def __init__(self,name,hp,speed,damage):
        Unit.__init__(self,name,hp,speed) #유닛 클래스에서 이름과 체력은 상속받음
        self.damage=damage 

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
        self.hp-=damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed=flying_speed

    def fly(self,name,location):
        print("{0} : {1} 뱡향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackunit(AttackUnit,Flyable):
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,0,damage) #지상 speed= 0
        Flyable.__init__(self,flying_speed)
    def move(self,location):
        print("[공중 유닛 이동]")
        self.fly(self.name,location)

#건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass # 일단 완성된 것 처럼 만드는 것

#서플라이 디폿
supply_depot = BuildingUnit('서플라이 디폿',500,'7시')

def game_start():
    print("[알림] 새로움 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()