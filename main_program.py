# Character Creator (Basic Ed.)
# Main program
import os.path
from character import Character

# check for external character info files
try:
    inf1 = open("character_races.txt", "r")
    inf2 = open("character_classes.txt", "r")
    inf3 = open("character_backgrounds.txt", "r")
except FileNotFoundError:
    raise  # stop program if any of the above files are missing from the directory

# import character race options, classes/jobs, and background options
# note: the D&D developers often add new character creation options; external files allow
# these long lists to be edited without touching the code
# races
race_string = inf1.read()
races = race_string.split("\n")

# classes
job_string = inf2.read()
jobs = job_string.split("\n")

# backgrounds
bg_string = inf3.read()
backgrounds = bg_string.split("\n")

# close all input files
inf1.close()
inf2.close()
inf3.close()

# user interaction start
print("DUNGEONS & DRAGONS 5th Edition Step-by-Step Character Creation (Basic Ed.)")
print("by Elliot Goldman")
print("--------------------------------------------------------------------------")
player = input("Your name >>> ")
new_char = Character(player, races, jobs, backgrounds)
print("Welcome, " + new_char.player_name + ".")
print("The first step to going on an adventure in Dungeons & Dragons is creating a character for yourself.")
print("A character is a combination of numerical game rules and your imagination. You will invent their personality,")
print("appearance, and backstory, and they will serve as your avatar in the game.")
print("But first, this walkthrough will cover some essential characteristics one at a time.")

# section 1 - race
print("\n--- 1. Choosing a Race ---")
print("\nEvery character belongs to a race, one of the many intelligent humanoid species in the D&D worlds.")
print("Do you want to [pick] a race, or get a [random] one?")
choosing = True
while choosing:
    nav = input(">>> ")
    if nav.lower() == "pick":
        new_char.pick_race()
        choosing = False
    elif nav.lower() == "random":
        new_char.random_race()
        choosing = False
    else:
        print("Please re-enter.")

# section 2 - character class /  job
print("\n--- 2. Choosing a Class ---")
print("\nEach adventurer is a member of a class. Class broadly describes a character's vocation, special talents,")
print("and the tactics they can employ when exploring the wilderness, fighting monsters, negotiating, etc.")
print("Do you wish to [pick] a class, or get a [random] one?")
choosing = True
while choosing:
    nav = input(">>> ")
    if nav.lower() == "pick":
        new_char.pick_job()
        choosing = False
    elif nav.lower() == "random":
        new_char.random_job()
        choosing = False
    else:
        print("Please re-enter.")

# section 3 - ability scores
print("\n--- 3. Determining Ability Scores ---")
print("\nMuch of what your character does in the game is influenced by one or more of the six abilities: Strength,")
print("Dexterity, Constitution, Intelligence, Wisdom, and Charisma.")
print("Each ability has a score to indicate how gifted you are in that area; higher is better.")
print("Finally, your ability score modifiers are derived from scores. Modifiers are the bonuses or penalties that")
print("influence the success or failure of your endeavors throughout your adventures.")
print("\nWill your D&D group [roll] for ability scores or use the [standard] array? Ask your Dungeon Master!")
choosing = True
while choosing:
    nav = input(">>> ")
    if nav.lower() == "roll":
        new_char.roll_ability_scores()
        new_char.assign_ability_scores()
        choosing = False
    elif nav.lower() == "standard":
        new_char.set_ability_scores(Character.STANDARD_ARRAY)
        new_char.assign_ability_scores()
        choosing = False
    else:
        print("Please re-enter.")

# section 4 - background
print("\n--- 4. Your Character's Background ---")
print("\nWhere do you come from? What was your life before you became an adventurer? Your background represents your")
print("previous occupation and/or your place in the D&D world. It could reveal a lot about how you view the world.")
print("Do you wish to [pick] a background, or get a [random] one?")
choosing = True
while choosing:
    nav = input(">>> ")
    if nav.lower() == "pick":
        new_char.pick_background()
        choosing = False
    elif nav.lower() == "random":
        new_char.random_background()
        choosing = False
    else:
        print("Please re-enter.")

# section 5 - name and traits
print("\n--- 5. More Details ---")
new_char.character_name = input("\nYour character's name >>> ")
print("Think about what", new_char.character_name, "looks like or what they're like as a person. Take a few notes")
print("here, in your own words. Press Enter when done.")
new_char.set_notes(input(">>> "))

# final revisions
print("\n--- Review ---")
print("\nYour character is " + new_char.character_name + ", the " + new_char.get_race(), new_char.get_job() + ".")
print("You have the " + new_char.get_background() + " background.")
print("Your ability scores:")
new_char.print_all_ability_scores()
revising = True
print("\nDo you wish to revise anything? If so, enter the number of the section to go back to. Hit Enter without a")
print("number to exit the program. Your character info will be saved as a .txt file in this folder.")
while revising:
    print("\n1. Race\n2. Class\n3. Ability Scores\n4. Background\n5. Name\n6. Character Notes")
    revision_menu = input(">>> ")
    if revision_menu == "":
        revising = False
    elif revision_menu == "1":
        print("\nDo you want to [pick] a race, or get a [random] one?")
        choosing = True
        while choosing:
            nav = input(">>> ")
            if nav.lower() == "pick":
                new_char.pick_race()
                choosing = False
            elif nav.lower() == "random":
                new_char.random_race()
                choosing = False
            else:
                print("Please re-enter.")
    elif revision_menu == "2":
        print("\nDo you wish to [pick] a class, or get a [random] one?")
        choosing = True
        while choosing:
            nav = input(">>> ")
            if nav.lower() == "pick":
                new_char.pick_job()
                choosing = False
            elif nav.lower() == "random":
                new_char.random_job()
                choosing = False
            else:
                print("Please re-enter.")
    elif revision_menu == "3":
        permission = input("\nThis will reset your ability scores and start over. Proceed? [y/n] >>> ")
        if permission.lower() == "y":
            new_char.reset_ab_scores()
            print("\nChoose [roll] for ability scores or the [standard] array.")
            choosing = True
            while choosing:
                nav = input(">>> ")
                if nav.lower() == "roll":
                    new_char.roll_ability_scores()
                    new_char.assign_ability_scores()
                    choosing = False
                elif nav.lower() == "standard":
                    new_char.set_ability_scores(Character.STANDARD_ARRAY)
                    new_char.assign_ability_scores()
                    choosing = False
                else:
                    print("Please re-enter.")
    elif revision_menu == "4":
        print("\nDo you wish to [pick] a background, or get a [random] one?")
        choosing = True
        while choosing:
            nav = input(">>> ")
            if nav.lower() == "pick":
                new_char.pick_background()
                choosing = False
            elif nav.lower() == "random":
                new_char.random_background()
                choosing = False
            else:
                print("Please re-enter.")
    elif revision_menu == "5":
        new_char.character_name = input("\nYour character's name >>> ")
    elif revision_menu == "6":
        print(new_char.character_name, "character notes - press Enter when done.")
        new_char.set_notes(input(">>> "))
    else:
        print("Invalid option, please re-enter.")

# character file creation
# note - for the sake of this project, assuming character_name does not contain any chars that
# are incompatible with the filepath; if any are present, this will not work
filename = new_char.character_name + ".txt"
save_character = True
if os.path.isfile(filename):
    print(filename, "already exists. Do you wish to save over your character? [y/n]")
    overwrite = input(">>> ")
    if overwrite.lower() == "n":
        save_character = False
if save_character:
    outfile = open(filename, "w")
    outfile.write("Player name: " + new_char.player_name)
    outfile.write("\nCharacter name: " + new_char.character_name)
    outfile.write("\n\nRace: " + new_char.get_race())
    outfile.write("\n\nClass: " + new_char.get_job())
    outfile.write("\n\nAbility Scores:")
    outfile.write("\nSTR " + str(new_char.get_strength()).rjust(2) + " ( " + "%+d" % Character.modifier(
        new_char.get_strength()) + " )")
    outfile.write("\nDEX " + str(new_char.get_dexterity()).rjust(2) + " ( " + "%+d" % Character.modifier(
        new_char.get_dexterity()) + " )")
    outfile.write("\nCON " + str(new_char.get_constitution()).rjust(2) + " ( " + "%+d" % Character.modifier(
        new_char.get_constitution()) + " )")
    outfile.write("\nINT " + str(new_char.get_intelligence()).rjust(2) + " ( " + "%+d" % Character.modifier(
        new_char.get_intelligence()) + " )")
    outfile.write("\nWIS " + str(new_char.get_wisdom()).rjust(2) + " ( " + "%+d" % Character.modifier(
        new_char.get_wisdom()) + " )")
    outfile.write("\nCHA " + str(new_char.get_charisma()).rjust(2) + " ( " + "%+d" % Character.modifier(
        new_char.get_charisma()) + " )")
    outfile.write("\n\nBackground: " + new_char.get_background())
    outfile.write("\n\nCharacter Notes:")
    outfile.write("\n" + new_char.get_notes())
    outfile.close()
