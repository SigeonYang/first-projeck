#일반유닛
from random import *


class Unit:
    def __init__(self,name,hp,speed):
        self.name = name 
        self.hp=hp 
        self.speed = speed
        print("{0} 유닛이 생성 되었습니다".format(name))
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
        self.hp-=damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

    
#공격유닛
class AttackUnit(Unit):
    def __init__(self,name,hp,speed,damage):
        Unit.__init__(self,name,hp,speed) #유닛 클래스에서 이름과 체력은 상속받음
        self.damage=damage 

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

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

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린",40,1,5)

    def stimpack(self):
        if self.hp > 10:
            self.hp-=10
            print  ("{0}: 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))

class Tank(AttackUnit):
    seize_developed=False #시즈모드 개발여부
    def __init__(self):
        AttackUnit.__init__(self,"탱크",150,1,35)
        self.seize_mod=False

    def set_mod(self):
        if Tank.seize_developed==False:
            return # 개발안됐으면 멈춰라

        if self.seize_mod==False:
            print("{0}: 시즈모드로 전환합니다.".format(self.name))
            self.damage*=2
            self.seize_mod=True
        else:
            print("{0}: 시즈모드로 해제합니다.".format(self.name))
            self.damage/=2
            self.seize_mod=False

class Wraith(FlyableAttackunit):
    def __init__(self):
        FlyableAttackunit.__init__(self,"레이스",80,20,5)
        self.clocked = False

    def clocking(self):
        if self.clocked==True:
            print("{0}:클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False
        else:
            print("{0}:클로킹 설정 합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로움 게임을 시작합니다.")

def game_over():
    print("Player : GG")
    print("Player 님이 나갔습니다.")

# 실제 게임 진행

game_start()
m1 = Marine()
m2 = Marine()
m3 = Marine()

t1=Tank()
t2=Tank()

w1 = Wraith()

#유닛 일괄 관리
attack_unit = []
attack_unit.append(m1)
attack_unit.append(m2)
attack_unit.append(m3)
attack_unit.append(t1)
attack_unit.append(t2)
attack_unit.append(w1)

for unit in attack_unit:
    unit.move("1시")

Tank.seize_developed = True
print ("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

#공격 모드 준비

for unit in attack_unit:
    if isinstance(unit,Marine):
        unit.stimpack

    elif isinstance(unit, Tank):
        unit.set_mod()

    elif isinstance(unit,Wraith):
        unit.clocking()

#전군 피해
for unit in attack_unit:
    unit.attack("1시")

for unit in attack_unit:
    unit.damaged(randint(5,20))

# 게임종료
game_over()