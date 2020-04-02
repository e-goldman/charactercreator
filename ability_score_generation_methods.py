# D&D Ability Score Generator
# Use this program to compare three common house rules for ability score generation with the Standard Array
# and Critical Role's campaign rule using a simple Monte Carlo simulation

import random


# Method 1 def
def roll_4d6_drop_lowest():
    scores = []
    for i in range(6):
        roll = []
        for j in range(4):
            roll.append(random.randint(1, 6))
        roll.remove(min(roll))
        scores.append(sum(roll))
    return scores


# Method 2 def
def roll_3d6_strict():
    scores = []
    for i in range(6):
        roll = []
        for j in range(3):
            roll.append(random.randint(1, 6))
        scores.append(sum(roll))
    return scores


# Method 3 def
def roll_2d6_plus_6():
    scores = []
    for i in range(6):
        roll = random.randint(1, 6) + random.randint(1, 6) + 6
        scores.append(roll)
    return scores


def main():
    NUM_TRIALS = 100000
    print("The standard array of fixed scores has a total of 72 points.")
    print("Critical Role features a variant of 4d6-drop-lowest with a mulligan if the total is fewer than 70 points.")
    print("How strong are the characters resulting from these methods in comparison to other rolling methods?")
    print("\nNumber of trials -", NUM_TRIALS)

    # Method 1 trial
    m1_less_than_std = 0
    m1_less_than_crit_role = 0
    for i in range(NUM_TRIALS):
        x = sum(roll_4d6_drop_lowest())
        if x < 72:
            m1_less_than_std += 1
        if x < 70:
            m1_less_than_crit_role += 1
    m1_std_percent = m1_less_than_std / NUM_TRIALS * 100
    m1_crit_percent = m1_less_than_crit_role / NUM_TRIALS * 100
    print("\nClassic 4d6 Drop Lowest rules:")
    print("Weaker than standard array " + str(round(m1_std_percent)) + "% of the time")
    print("Weaker than CritRole's min score total " + str(round(m1_crit_percent)) + "% of the time")

    # Method 2 trial
    m2_less_than_std = 0
    m2_less_than_crit_role = 0
    for i in range(NUM_TRIALS):
        x = sum(roll_3d6_strict())
        if x < 72:
            m2_less_than_std += 1
        if x < 70:
            m2_less_than_crit_role += 1
    m2_std_percent = m2_less_than_std / NUM_TRIALS * 100
    m2_crit_percent = m2_less_than_crit_role / NUM_TRIALS * 100
    print("\nStrict 3d6 rules:")
    print("Weaker than standard array " + str(round(m2_std_percent)) + "% of the time")
    print("Weaker than CritRole's min score total " + str(round(m2_crit_percent)) + "% of the time")

    # Method 3 trial
    m3_less_than_std = 0
    m3_less_than_crit_role = 0
    for i in range(NUM_TRIALS):
        x = sum(roll_2d6_plus_6())
        if x < 72:
            m3_less_than_std += 1
        if x < 70:
            m3_less_than_crit_role += 1
    m3_std_percent = m3_less_than_std / NUM_TRIALS * 100
    m3_crit_percent = m3_less_than_crit_role / NUM_TRIALS * 100
    print("\nLow-risk 2d6+6 rules:")
    print("Weaker than standard array " + str(round(m3_std_percent)) + "% of the time")
    print("Weaker than CritRole's min score total " + str(round(m3_crit_percent)) + "% of the time")


# Main function call
main()