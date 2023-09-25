import random

def roll_dice(num_dice, num_sides):
    total = 0
    for _ in range(num_dice):
        roll = random.randint(1, num_sides)
        total += roll
    return total

def display_stats(modifiers):
    print("\n---")
    print("Player Stats:")
    print("--------------")
    print(f"Speed: {modifiers[0]}")
    print(f"Strength: {modifiers[1]}")
    print(f"Intelligence: {modifiers[2]}")
    print("--------------")

def get_user_input(prompt, valid_inputs):
    while True:
        choice = input(prompt)
        try:
            choice = int(choice)
            if choice in valid_inputs:
                return choice
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid choice. Try again.")

def play_adventure_game():
    print("Welcome to the Adventure Game!")
    player_name = input("Enter your name: ")
    print("There is a jealousy king who does not want you to marry his son.")
    print("However, both of you liked each other.")
    print("Finally, tomorrow is the day of the wedding.")
    print("You were too nervous, thus you could not sleep enough.")
    print("However, the kidnapper came into your room and kidnapped you.")
    print("Therefore, after you woke up from the deep sleep, you were in a mysterious place.")
    print("What would you do in this situation?")
    print(f"Hello, {player_name}! Let's begin the adventure.")

    modifiers = []
    for _ in range(3):
        modifier = roll_dice(4, 6) // 5
        modifiers.append(modifier)

    successful_scenarios = 0
    game_over = False

    while not game_over:
        print("\n---")
        print("Encounter a kidnapper or Obstacle!")
        print("Choose one of the following options:")
        print("1. Sneak out from the kidnapper (Difficulty: 12, Skill: Speed)")
        print("2. Engage in combat with the kidnapper (Difficulty: 15, Skill: Strength)")
        print("3. Solve a riddle (Difficulty: 10, Skill: Intelligence)")

        choice = get_user_input("Enter your choice (1/2/3): ", [1, 2, 3])

        difficulty = 0
        skill_modifier = 0

        if choice == 1:
            difficulty = 12
            skill_modifier = modifiers[0]
        elif choice == 2:
            difficulty = 15
            skill_modifier = modifiers[1]
        elif choice == 3:
            difficulty = 10
            skill_modifier = modifiers[2]

        print("\n---")
        print("Rolling the dice...")
        roll = roll_dice(1, 20)
        total = roll + skill_modifier

        print(f"You rolled: {roll}")
        print(f"Total (Roll + Modifier): {total}")
        print(f"Difficulty: {difficulty}")

        if total >= difficulty:
            print("\n---")
            print("Congratulations! You succeeded in the challenge.")
            successful_scenarios += 1
        else:
            print("\n---")
            print("Oh no! You failed the challenge.")
            print("GAME OVER")
            play_again = input("Do you want to play again? (yes/no): ")

            if play_again.lower() == "no":
                game_over = True

            else:
                # Reset game variables and generate new modifiers
                successful_scenarios = 0
                modifiers = []
                for _ in range(3):
                    modifier = roll_dice(4, 6) // 5
                    modifiers.append(modifier)

    if successful_scenarios == 3:
        print("\n---")
        print("Congratulations! You have successfully completed the adventure!")
        print(f"{player_name}, you won by completing 3 scenarios.")

    # Final Boss Encounter
    print("\n---")
    print("You encounter the Final Boss!")
    print("Prepare for the ultimate challenge!")

    # Final Boss Encounter
    print("\n---")
    print("You encounter the Final Boss the king!")
    print("Prepare for the ultimate challenge!")

    boss_armor = 18
    boss_health = 50
    player_health = 30

    while boss_health > 0 and player_health > 0:
        print("\n---")
        print("It's your turn to attack!")

        print("Rolling the dice...")
        attack_roll = roll_dice(1, 20)
        attack_total = attack_roll + modifiers[1]

        if attack_roll == 20:  # Natural 20, double damage
            damage = roll_dice(1, 12) * 2
            print("Critical hit! Double damage dealt!")
        else:
            damage = roll_dice(1, 12)

        print(f"You rolled: {attack_roll}")
        print(f"Total Attack (Roll + Strength Modifier): {attack_total}")
        print(f"You dealt {damage} damage to the boss.")

        boss_armor -= damage

        if boss_armor <= 0:
            print("\n---")
            print("Congratulations! You defeated the Final Boss King!")
            print(f"{player_name}, you have completed the adventure!")

            print("\n---")
            print("GAME OVER")
            play_again = input("Do you want to play again? (yes/no): ")

            if play_again.lower() == "no":
                break
            else:
                # Reset game variables and generate new modifiers
                successful_scenarios = 0
                modifiers = []
                for _ in range(3):
                    modifier = roll_dice(4, 6) // 5
                    modifiers.append(modifier)

        else:
            print("\n---")
            print("It's the king's turn to attack!")

            boss_attack_roll = roll_dice(1, 20)
            boss_attack_total = boss_attack_roll + 3  # Boss attack modifier

            if boss_attack_roll == 20:  # Boss critical hit
                boss_damage = roll_dice(1, 12) * 2
                print("King landed a critical hit! Double damage received!")
            else:
                boss_damage = roll_dice(1, 12)

            print(f"The boss rolled: {boss_attack_roll}")
            print(f"Total Boss Attack (Roll + Modifier): {boss_attack_total}")
            print(f"The boss dealt {boss_damage} damage to you.")

            player_health -= boss_damage

            if player_health <= 0:
                print("\n---")
                print("Oh no! The boss defeated you.")
                print("GAME OVER")
                play_again = input("Do you want to play again? (yes/no): ")

                if play_again.lower() == "no":
                    break
                else:
                    # Reset game variables and generate new modifiers
                    successful_scenarios = 0
                    modifiers = []
                    for _ in range(3):
                        modifier = roll_dice(4, 6) // 5
                        modifiers.append(modifier)

    print("\n---")
    print("Thank you for playing the Adventure Game!")

play_adventure_game()