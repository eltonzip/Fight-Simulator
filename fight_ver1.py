from random import randint

class TTarget:
    health = int
    name = str

    def __init__(self, name, health):
        self.hp = health
        self.nm = name

    def statscheck(self):
        print(self.nm)
        print(self.hp)

    def attack(self, target, target1):
        if target1.hp > 0:
            target1.hp -= 20
            print(target.nm, "has attacked", target1.nm + "!")
            print(target1.nm + "'s health is now", target1.hp)
        if target1.hp <= 0:
            print(target1.nm, "is dead!", target.nm, "has won!")
            exit()
    
Warrior1 = TTarget("John", 100)
Warrior2 = TTarget("Mary", 100)

Q = 0

while True:
    Q = int(input("1(attack) or 2(exit) or 3(stats): "))

    if Q == 2:
        exit()
    elif Q == 3:
        nuw = int(input("Wich one of two: "))
        if nuw == 1:
            Warrior1.statscheck()
        else:
            Warrior2.statscheck()
    elif Q == 1:
        AttCnst = randint(1, 2+1)
        if AttCnst == 2:
            Warrior1.attack(Warrior1, Warrior2)
        else:
            Warrior2.attack(Warrior2, Warrior1)

    print("-"*len("1(attack) or 2(exit) or 3(stats): "))
