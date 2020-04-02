# Class Definition - Character class
import random


class Character:

    # A Dungeons & Dragons character has 6 abilities: Strength, Dexterity, Constitution, Intelligence, Wisdom,
    # and Charisma. Each ability has a score which influences the success or failure of related actions in the game.
    # Most groups of players roll dice to determine their ability scores, but some use the predetermined scores
    # from the following list, known as the standard array.
    STANDARD_ARRAY = [15, 14, 13, 12, 10, 8]

    # An ability score's modifier is the bonus or penalty it applies to associated character skills, attacks, etc
    # it's calculated via following rule: modifier = (ability score - 10) // 2
    @staticmethod
    def modifier(score):
        return (score - 10) // 2

    # Characters
    def __init__(self, player_name, races, jobs, backgrounds):
        self.player_name = player_name
        self.character_name = None
        self.__races = races
        self.__character_race = None
        self.__jobs = jobs  # a career or specialization is a 'class' in D&D rules; using 'job' here to avoid confusion
        self.__character_job = None
        self.__ability_scores = []
        self.__strength = 0
        self.__dexterity = 0
        self.__constitution = 0
        self.__intelligence = 0
        self.__wisdom = 0
        self.__charisma = 0
        self.__backgrounds = backgrounds
        self.__character_background = None
        self.__notes = None

    def __repr__(self):
        return "Character(%s, %s, %s, %s, %s, %s, %s, %d, %d, %d, %d, %d, %d, %s, %s, %s)" \
               % (self.player_name, self.character_name, self.__races, self.__character_race, self.__jobs,
                  self.__character_job, self.__ability_scores, self.__strength, self.__dexterity, self.__constitution,
                  self.__intelligence, self.__wisdom, self.__charisma, self.__backgrounds, self.__character_background,
                  self.__notes)

    def set_race(self, race):
        self.__character_race = race

    def get_race(self):
        return self.__character_race

    def set_job(self, job):
        self.__character_job = job

    def get_job(self):
        return self.__character_job

    def set_ability_scores(self, scores):
        self.__ability_scores = scores

    def get_ability_scores(self):
        return self.__ability_scores

    def __set_strength(self, strn):
        self.__strength = strn

    def get_strength(self):
        return self.__strength

    def __set_dexterity(self, dex):
        self.__dexterity = dex

    def get_dexterity(self):
        return self.__dexterity

    def __set_constitution(self, con):
        self.__constitution = con

    def get_constitution(self):
        return self.__constitution

    def __set_intelligence(self, intel):
        self.__intelligence = intel

    def get_intelligence(self):
        return self.__intelligence

    def __set_wisdom(self, wis):
        self.__wisdom = wis

    def get_wisdom(self):
        return self.__wisdom

    def __set_charisma(self, cha):
        self.__charisma = cha

    def get_charisma(self):
        return self.__charisma

    def print_all_ability_scores(self):
        print("\tSTR", str(self.__strength).rjust(2), "(", "%+d" % Character.modifier(self.__strength), ")")
        print("\tDEX", str(self.__dexterity).rjust(2), "(", "%+d" % Character.modifier(self.__dexterity), ")")
        print("\tCON", str(self.__constitution).rjust(2), "(", "%+d" % Character.modifier(self.__constitution), ")")
        print("\tINT", str(self.__intelligence).rjust(2), "(", "%+d" % Character.modifier(self.__intelligence), ")")
        print("\tWIS", str(self.__wisdom).rjust(2), "(", "%+d" % Character.modifier(self.__wisdom), ")")
        print("\tCHA", str(self.__charisma).rjust(2), "(", "%+d" % Character.modifier(self.__charisma), ")")

    def set_background(self, background):
        self.__character_background = background

    def get_background(self):
        return self.__character_background

    def set_notes(self, notes_string):
        self.__notes = notes_string

    def get_notes(self):
        return self.__notes

    # generates 6 weighted random ints via following rule: roll four 6-sided dice, drop the lowest, sum remaining three
    # the list is assigned to ability_scores to keep a record of what was rolled and to ab_sc_copy for manipulation
    def roll_ability_scores(self):
        scores = []
        for i in range(6):
            roll = []
            for j in range(4):
                roll.append(random.randint(1, 6))
            roll.remove(min(roll))
            scores.append(sum(roll))
        self.set_ability_scores(scores)

    # validates user input for ability to assign score, calls add_score() method to perform assignment
    def assign_ability_scores(self):
        for i in range(6):
            print("\nAbility scores:", self.__ability_scores)
            print("Assign a score to an ability by entering the ability's abbreviation and then the score.")
            print("\tSTR", self.__strength, "\n\tDEX", self.__dexterity, "\n\tCON", self.__constitution, "\n\tINT",
                  self.__intelligence, "\n\tWIS", self.__wisdom, "\n\tCHA", self.__charisma)
            choosing = True
            while choosing:
                ab = input("Ability >>> ")
                if ab.upper() == "STR":
                    if self.__strength == 0:
                        self.__strength = self.__add_score()
                        choosing = False
                    else:
                        print("Already assigned, please re-enter.")
                elif ab.upper() == "DEX":
                    if self.__dexterity == 0:
                        self.__dexterity = self.__add_score()
                        choosing = False
                    else:
                        print("Already assigned, please re-enter.")
                elif ab.upper() == "CON":
                    if self.__constitution == 0:
                        self.__constitution = self.__add_score()
                        choosing = False
                    else:
                        print("Already assigned, please re-enter.")
                elif ab.upper() == "INT":
                    if self.__intelligence == 0:
                        self.__intelligence = self.__add_score()
                        choosing = False
                    else:
                        print("Already assigned, please re-enter.")
                elif ab.upper() == "WIS":
                    if self.__wisdom == 0:
                        self.__wisdom = self.__add_score()
                        choosing = False
                    else:
                        print("Already assigned, please re-enter.")
                elif ab.upper() == "CHA":
                    if self.__charisma == 0:
                        self.__charisma = self.__add_score()
                        choosing = False
                    else:
                        print("Already assigned, please re-enter.")
                else:
                    print("Ability not recognized, please re-enter.")
        print("\nYour ability scores and modifiers:")
        print("\tSTR", str(self.__strength).rjust(2), "(", "%+d" % Character.modifier(self.__strength), ")")
        print("\tDEX", str(self.__dexterity).rjust(2), "(", "%+d" % Character.modifier(self.__dexterity), ")")
        print("\tCON", str(self.__constitution).rjust(2), "(", "%+d" % Character.modifier(self.__constitution), ")")
        print("\tINT", str(self.__intelligence).rjust(2), "(", "%+d" % Character.modifier(self.__intelligence), ")")
        print("\tWIS", str(self.__wisdom).rjust(2), "(", "%+d" % Character.modifier(self.__wisdom), ")")
        print("\tCHA", str(self.__charisma).rjust(2), "(", "%+d" % Character.modifier(self.__charisma), ")")

    # validates user input, removes input value from ab_sc_copy list if present, returns int value
    def __add_score(self):
        choosing = True
        while choosing:
            sc = eval(input("Score >>> "))
            for i in range(len(self.__ability_scores)):
                if sc == self.__ability_scores[i]:
                    self.__ability_scores.remove(sc)
                    return sc
            print("Invalid, please re-enter.") # above conditional statement causes method to return before this prints

    def reset_ab_scores(self):
        self.__strength = self.__dexterity = self.__constitution = self.__intelligence = self.__wisdom = self.__charisma = 0

    # prints race choices, validates user input, assigns to character_race attribute
    def pick_race(self):
        print("\nCharacter Races:")
        for i in range(len(self.__races)):
            print(" - ", self.__races[i])
        choosing = True
        while choosing:
            choice = input("Your choice >>> ")
            for i in range(len(self.__races)):
                if choice.lower() == self.__races[i].lower():
                    self.set_race(self.__races[i])
                    print("\nYour race is " + self.get_race() + "!")
                    choosing = False
            if choosing:
                print("Race not found, please re-enter.")

    # assigns random element from races list to character_race attribute
    def random_race(self):
        self.set_race(random.choice(self.__races))
        print("\nYour race is " + self.get_race() + "!")

    # prints character class choices, validates user input, assigns to character_class attribute
    def pick_job(self):
        print("\nCharacter Classes:")
        for i in range(len(self.__jobs)):
            print(" - ", self.__jobs[i])
        choosing = True
        while choosing:
            choice = input("Your choice >>> ")
            for i in range(len(self.__jobs)):
                if choice.lower() == self.__jobs[i].lower():
                    self.set_job(self.__jobs[i])
                    print("\nYour class is " + self.get_job() + "!")
                    choosing = False
            if choosing:
                print("Class not found, please re-enter.")

    # assigns random element from list of character classes to the character_class attribute
    def random_job(self):
        self.set_job(random.choice(self.__jobs))
        print("\nYour class is " + self.get_job() + "!")

    # prints character background choices, validates user input, assigns to character_background attribute
    def pick_background(self):
        print("\nCharacter Backgrounds:")
        for i in range(len(self.__backgrounds)):
            print(" - ", self.__backgrounds[i])
        choosing = True
        while choosing:
            choice = input("Your choice >>> ")
            for i in range(len(self.__backgrounds)):
                if choice.lower() == self.__backgrounds[i].lower():
                    self.set_background(self.__backgrounds[i])
                    print("\nYou have the " + self.get_background() + " background!")
                    choosing = False
            if choosing:
                print("Background not recognized, please re-enter.")

    # assigns random element from list of character backgrounds to the character_background attribute
    def random_background(self):
        self.set_background(random.choice(self.__backgrounds))
        print("\nYou have the " + self.get_background() + " background!")
