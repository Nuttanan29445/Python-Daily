class Warrior :
    def __init__(self,powwer,defend,hp):
        self.powwer = powwer
        self.hp = hp
        self.defend = defend
    def attack(self,warriorObj):
        if(self.powwer > warriorObj.defend):
            n = warriorObj.hp
            warriorObj.hp = n-(self.powwer  - warriorObj.defend) 
        if warriorObj.hp == 0:
            print("Enemy died")

Warrior_A = Warrior(100, 50, 80)
Warrior_B = Warrior(60, 80, 120)
print("=== Before Attack===")
print("Warrior_A HP = ", Warrior_A.hp)
print("Warrior_B HP = ", Warrior_B.hp)
Warrior_A.attack(Warrior_B)
Warrior_B.attack(Warrior_A)
print("=== After Attack===")
print("Warrior_A HP = ", Warrior_A.hp)
print("Warrior_B HP = ", Warrior_B.hp)