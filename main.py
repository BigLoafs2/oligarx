import random

class NPC:
    def __init__(self, base_resist, armor_resist, health):
        self.resist = base_resist + armor_resist
        self.fire_resist = random.randrange(0, 30)
        self.cold_resist = random.randrange(0, 30)
        self.health = health

    isDead = False

    def getDamage(self, damage_d):
        self.health -= damage_d
        if self.health <=0:
            self.isDead = True
        return damage_d

def damage(NPC, damage_type, base_damage = 0, fire_damage = 0, cold_damage = 0):
    if damage_type == 0:
        d =  (base_damage - NPC.resist) + (fire_damage - NPC.fire_resist ) + (cold_damage - NPC.cold_resist)
        return d if d > 0 else 0
    else:
        d = (fire_damage - NPC.fire_resist ) + (cold_damage - NPC.cold_resist)
        return d if d > 0 else 0

oleg = NPC(30, 60, 190)

while True:
    action = input("Тип  урона: ")
    if action.upper() == "Оружие".upper():
        d = int(input("Кол-во урона огнём: "))
        df = oleg.getDamage(damage(oleg, 0, d))
        print("Нанесено урона:", df)
        print("Осталось здоровья", oleg.health)
        if oleg.health <= 0:
            print("Попуск")

    elif action.upper() == "Холод".upper:
        d = int(input("Кол-во урона оружием: "))
        v = int(input("Кол-во урона холодом: "))
        df = oleg.getDamage(damage(oleg, 0, d))
        print("Нанесено урона:", df)
        print("Осталось здоровья", oleg.health)
        if oleg.health <= 0:
            print("Попуск")

    elif action.upper() == "Огонь".upper:
        d = int(input("Кол-во урона оружием: "))
        v = int(input("Кол-во урона холодом: "))
        с = int(input("Кол-во урона огнем "))
        df = oleg.getDamage(damage(oleg, 0, d))
        print("Нанесено урона:", df)
        print("Осталось здоровья", oleg.health)
        if oleg.health <= 0:
            print("Попуск")

