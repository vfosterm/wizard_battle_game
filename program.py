
from actors import *


def main():
    print_header()
    game_loop()


def print_header():
    print("----------------------------")
    print("       Wizard Battle")
    print("----------------------------")


def game_loop():
    hero_name = input("Name your Wizard: ")
    rival_name = input("Enter the name of your sworn enemy: ")
    base_level = 50
    base_xp = base_level * 10
    hero = Wizard(hero_name, base_xp, 10)
    enemies = [Creature('Wolf', 100),
               Creature('Giant Crab', 200),
               Creature('Mouse', 10),
               Creature('Giant Crab', 200),
               Creature('Wolf', 150),
               Golom('Giant Rock Golom', 300),
               Golom('Rock Golom', 200),
               Golom('Mud Golom', 100),
               Dragon('Fire Dragon', 350),
               Dragon('Ice Dragon', 500),
               Creature('Rodent of Unusual Size', 400),
               EvilWizard(rival_name, 800)
               ]
    time.sleep(1)
    print('----------------------------')
    print("Your sworn enemy {} has taken over your sacred tower and filled it \n".format(rival_name) +
          "with foul creatures. Go forth and destroy them all!")
    time.sleep(2)
    while True:
        active_actor = random.choice(enemies)
        print('----------------------------')
        if active_actor.name == rival_name:
            print("Your sworn enemy {} confronts you in the labyrinth!!!".format(active_actor.name))
            time.sleep(1)
        else:
            print('A {} confronts you in the labyrinth'.format(active_actor.name))
            time.sleep(1)
        cmd = input("Do you [a]ttack, [r]un, or [m]editate?")
        print('----------------------------')
        previous_level = hero.level
        if cmd == 'a':
            battle = attack(hero, active_actor)
            if battle == 'attacker_win':
                print(hero.name, 'was victorious and has gained {} XP'.format(active_actor.xp_granted))
                hero.xp += active_actor.xp_granted
                hero.level = math.floor(hero.xp/10)
                hero.hp = hero.level * 20
                if previous_level < hero.level:
                    print("{} has Leveled up!".format(hero.name))
                    time.sleep(1)
                    hero.__repr__()
                print(hero.name, "casts a spell to heal their wounds")
                enemies.remove(active_actor)
            if battle == 'defender_win':
                print('!!!!!!!GAME_OVER!!!!!!!')
                break
        elif cmd == 'r':
            print('RUN!!!')
        elif cmd == 'm':
            hero.__repr__()

        elif cmd == 'x':
            break
        else:
            print("{} stands there with a strangely vacant look in their eyes. {} ran away".format(hero.name, active_actor.name))
        if not enemies:
            print('!!!!!You have defeated evil in the labyrinth!!!!!')
            break


if __name__ == '__main__':
    main()
