# charactercreator
DnD 5e Character Creation Tool

For my Info Structures with Python term project at BU, I set out to make a companion application for the pen-and-paper roleplaying
game Dungeons & Dragons.

The first thing you need to do if you're going to play D&D with a group of friends is make a character that will represent you
in the fantasy world. The character's personal details are defined by a mix of using your imagination, rolling dice, and making
some choices from lists of available options (e.g. is your character a dwarf? an elf?). The project is calibrated for use by 
new players who need help getting started, so it's designed as a step-by-step, guided process.

---Usage instructions---

Run 'main_program.py' to create a character

Run 'ability_score_generation_methods.py' for a Monte Carlo sim comparing common house rules for determining character abilities
and how powerful resulting characters are likely to be

---Updates---

Next update:
- Integrate remaining ability score generation rulesets from 'ability_score_generation_methods.py' into character creator
- Integrate racial ability score modifiers (e.g. half-elves get +2 charisma and +1 to two other abilities of the player's choice)

Goals:
- Continue adding charcter creation steps and incorporating more of D&D's rules into the application
- Output saved characters to form-fillable PDFs instead of .txt files
- Long-term - make an executable with a UI to make the program more accessible
