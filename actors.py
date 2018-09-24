import math
import random
import time


class Actor:

    def __init__(self, name, experience_points):
        self.name = name
        self.xp = experience_points
        self.level = math.floor(experience_points/10)
        self.hp = self.level * 10


class Wizard(Actor):

    def __init__(self, name, experience_points, crit_chance):
        super().__init__(name, experience_points)
        self.crit_chance = crit_chance
        self.hp = self.level * 20

    def __repr__(self):
        print('----------------------------')
        print('Wizard: {}'.format(self.name))
        print('Health: {}'.format(self.hp))
        print('Level: {}'.format(self.level))
        print('Max Damage: {}'.format(str(12*self.level*1.5)))
        print('----------------------------')

    def is_crit(self, crit_chance):
        crit = 100 - crit_chance
        roll = random.randint(0, 100)
        if roll >= crit:
            print('!!!CRITICAL HIT!!!')
            return True
        else:
            return False

    def get_attack(self, crit_chance):
        attack_roll = random.randint(1, 12)

        if self.is_crit(crit_chance):

            return int(12*self.level*1.5)
        else:
            return attack_roll*self.level


class Creature(Actor):
    def __init__(self, name, experience_points):
        super().__init__(name, experience_points)
        self.xp_granted = int(self.level*.8)

    def get_attack(self):
        attack_roll = random.randint(1, 12)
        return attack_roll * self.level


class Golom(Actor):
    def __init__(self, name, experience_points):
        super().__init__(name, experience_points)
        self.xp_granted = int(self.level*.9)
        self.hp = self.level * 40

    def get_attack(self):
        attack_roll = random.randint(1, 12)
        return attack_roll * self.level


class Dragon(Actor):
    def __init__(self, name, experience_points):
        super().__init__(name, experience_points)
        self.xp_granted = int(self.level)
        self.hp = self.level * 25

    def get_attack(self):
        attack_roll = random.randint(1, 12)
        return int(attack_roll * self.level * random.uniform(1, 1.5))


class EvilWizard(Actor):
    def __init__(self, name, experience_points):
        super().__init__(name, experience_points)
        self.xp_granted = int(self.level*2)
        self.hp = self.level * 10

    def get_attack(self):
        attack_roll = random.randint(1, 12)
        return int(attack_roll * self.level * random.uniform(1, 2.5))


def attack(attacker, defender):
    while True:
        attacker_power = attacker.get_attack(attacker.crit_chance)
        print(attacker.name, "attacks", defender.name, "for:", str(attacker_power), "Damage")
        defender.hp -= attacker_power
        time.sleep(1)
        if defender.hp < 0:
            defender.hp = 0
        print(defender.name, "has", str(defender.hp), 'HP left')
        print('----------------------------')
        time.sleep(2)
        if defender.hp > 0:
            defender_power = defender.get_attack()
            print(defender.name, "attacks", attacker.name, "for:", str(defender_power), "Damage")
            attacker.hp -= defender_power
            time.sleep(1)
            if attacker.hp <= 0:
                attacker.hp = 0
                print(attacker.name, "has", str(attacker.hp), 'HP left')
                time.sleep(2)
                print("!!!!!!!YOU_DIED!!!!!!!!")
                return 'defender_win'

            print(attacker.name, "has", str(attacker.hp), 'HP left')
            print('----------------------------')
            time.sleep(2)
        elif defender.hp <= 0:
            return 'attacker_win'



















