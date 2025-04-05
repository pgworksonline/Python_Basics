# The game involves one player and one mosnter
# The player begins with 100 health, while the monster starts with 150 health
# If the player attacks, they deal between 10-15 damage to the monster
# If the player heals, they regain 30 health but can't exceed a maximum of 100
# If the player runs away, the game concludes
# After the players turn, if the monster is still alaive, it deals betewen 15 and 20 damage to the player
# The game continues until the health of either the player or the mosnter reaches 0, or until the player decides to runaway
# Prevent the player from exiting the game by pressing CTRL+C
# Introduce double-damage criticla hists that occur when an attack value is a multiple of 3
# Use Emojis or string formatting syntax to make the game output more enjoyable

from random import randint

player_health = 100
monster_health = 150
heal = 30

def is_factor_of_three(number):
    if number % 3 == 0:
        return True
    else:
        return False

def calculate_damage_dealt_by(attacker):
    if attacker == "player":
        damage = randint(10, 15)
        
    else: # Monster
        damage = randint(15, 20)
        
    if is_factor_of_three(damage):
        damage = damage * 2
        print(f"💥 {attacker.capitalize()} scored a Critical Hit!")
        
    return damage

print("Welcome to the role-playing game!")


    
while True:
    print(f"❤️ Your health is: {player_health} 🐉 The Monster health is: {monster_health}")
    try:
        action = input("What would you like to do? You can (A)ttack, (H)eal, or (R)unway: ").upper()
    except KeyboardInterrupt:
        print("❌You can't exit using CTRL+C")
        continue


    # Player
    if action == "A":
        damage = calculate_damage_dealt_by("player")
        monster_health -= damage
        print(f"🦸🏼‍♂️ You attacked the Monster with {damage} damage!")

        if monster_health <= 0:
            print("🏆You defeated the Monster!")
            break

    elif action == "H":
        player_health += heal
        if player_health > 100:
            player_health = 100
        print(f"❤️‍🩹 Player health was healed by {heal} health!")

    elif action == "R":
        print("You ran away!")
        break

    else:
        print("You did not select an appropriate action!")
        print("You must choose (A), (H), or (R)")
        continue
        
    # Monster
    if monster_health > 0:
        monster_damage = calculate_damage_dealt_by("monster")
        player_health -= monster_damage
        print(f"🐲 The monster attacked and caused {monster_damage} damage!")

        if player_health <= 0:
            print("☠️You were defeated by the Monster!")
            break
